# ================================
# AI-Powered Customer Chat Insight Generator
# ================================

# --- Import Libraries ---
import os
import re
import json
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import plotly.express as px

# --- Configuration ---
PROMPT_PATH = "prompts/summarizer_prompt.txt"  # Custom prompt template path
DEFAULT_MODEL = "gpt-3.5-turbo"                # Default LLM model
ALLOWED_MODELS = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o"]  # Models user can choose from

# ================================
# API Setup
# ================================
@st.cache_resource
def get_client():
    """Load API key from .env and initialize OpenAI client."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

# ================================
# Prompt Loader
# ================================
@st.cache_data
def load_prompt(path: str) -> str:
    """Load base prompt from file (or use default fallback)."""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "Summarize the customer message, detect sentiment, and suggest an action in JSON."

# ================================
# Output Parsing Helpers
# ================================
def safe_extract_json(text: str):
    """Try to extract JSON safely from model output."""
    start, depth = None, 0
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                candidate = text[start:i+1]
                try:
                    return json.loads(candidate)
                except Exception:
                    start = None
    # Fallback attempt
    try:
        return json.loads(text.strip().strip("`"))
    except Exception:
        return None

def fallback_parse_plain_text(text: str):
    """Fallback: extract summary, sentiment, and action with regex if no JSON found."""
    result = {"customer_summary": "", "sentiment": "Unknown", "suggested_action": ""}
    m_sum = re.search(r"Customer Summary:\s*(.+?)(?:\n[A-Z][a-z]+:|$)", text, re.S)
    if m_sum: result["customer_summary"] = m_sum.group(1).strip()
    m_sent = re.search(r"Sentiment:\s*([A-Za-z]+)", text)
    if m_sent: result["sentiment"] = m_sent.group(1).strip()
    m_act = re.search(r"Suggested Action:\s*(.+?)(?:\n|$)", text)
    if m_act: result["suggested_action"] = m_act.group(1).strip()
    return result

# ================================
# Prompt Builder
# ================================
def build_prompt(base_prompt: str, message: str, language: str = "English"):
    """Build final prompt for model with message and language setting."""
    return f"{base_prompt}\n\nCustomer Message:\n{message}\n\nRespond in: {language}"

# ================================
# Get AI Response
# ================================
def get_response(client, prompt: str, model: str = DEFAULT_MODEL):
    """Send prompt to chosen model and return response text."""
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# ================================
# Streamlit UI Setup
# ================================
st.set_page_config(page_title="ChatInsight AI", layout="wide")
st.title("AI-Powered Customer Chat Insight Generator")
st.caption("Upload your customer chat data → Get insights in seconds.")  
# --- Initialize API Client ---
client = get_client()
if client is None:
    st.error("❌ API key not found. Add OPENAI_API_KEY to your .env.")
    st.stop()

# --- Load prompt template ---
base_prompt = load_prompt(PROMPT_PATH)

# ================================
# File Upload Section
# ================================
uploaded_file = st.file_uploader("Upload CSV with `Customer` and `Message` columns", type="csv")
use_sample = st.checkbox("Use sample data (data/sample_chats.csv)")

# ================================
# Model & Language Selection
# ================================
model_choice = st.selectbox("Choose model", ALLOWED_MODELS, index=0)
language_choice = st.selectbox(
    "Insight Language", 
    ["English", "Spanish", "French", "German", "Arabic", "Chinese"], 
    index=0
)

# ================================
# Data Handling
# ================================
df = None
if use_sample and os.path.exists("data/sample_chats.csv"):
    df = pd.read_csv("data/sample_chats.csv")
elif uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        st.error("Could not read the uploaded CSV. Ensure it is a valid CSV file.")

# ================================
# Generate Insights
# ================================
if df is not None:
    if "Customer" not in df.columns or "Message" not in df.columns:
        st.error("CSV must contain 'Customer' and 'Message' columns.")
    else:
        st.subheader("📂 File Preview")
        st.dataframe(df.head())

        if st.button("Generate Insights"):
            total = len(df)
            progress = st.progress(0)
            out_rows = []

            for i, row in df.iterrows():
                # Build prompt
                prompt = build_prompt(base_prompt, str(row["Message"]), language_choice)
                
                # Get response
                raw = get_response(client, prompt, model_choice)
                
                # Parse structured output
                parsed = safe_extract_json(raw)
                if parsed is None:
                    parsed = fallback_parse_plain_text(raw)

                out_rows.append({
                    "Customer": row["Customer"],
                    "Message": row["Message"],
                    "AI Insight (raw)": raw,
                    "Customer Summary": parsed.get("customer_summary") or parsed.get("Customer Summary") or "",
                    "Sentiment": parsed.get("sentiment") or parsed.get("Sentiment") or "Unknown",
                    "Suggested Action": parsed.get("suggested_action") or parsed.get("Suggested Action") or ""
                })
                progress.progress((i+1)/total)

            st.success("Insights generated.")
            st.session_state["insight_data"] = pd.DataFrame(out_rows)

# ================================
# Dashboard & Results
# ================================
if st.session_state.get("insight_data") is not None:
    df_out = st.session_state["insight_data"]

    # --- Sentiment Distribution ---
    st.subheader("Sentiment Distribution")
    sentiment_counts = df_out["Sentiment"].value_counts(normalize=True) * 100
    if not sentiment_counts.empty:
        sent_df = pd.DataFrame({"Sentiment": sentiment_counts.index, "Percentage": sentiment_counts.values})
        fig_sent = px.bar(
            sent_df, x="Sentiment", y="Percentage", 
            title="Sentiment Distribution", text="Percentage"
        )
        fig_sent.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        st.plotly_chart(fig_sent, use_container_width=True)

    # --- Detailed Insights ---
    st.subheader("Detailed Insights")

    # Filter by sentiment
    sentiments = sorted(df_out["Sentiment"].unique())
    sentiment_filter = st.multiselect("Filter by Sentiment", sentiments, default=sentiments)
    filtered = df_out[df_out["Sentiment"].isin(sentiment_filter)]

    # Group by customer toggle
    group_by = st.checkbox("Group by Customer")
    if group_by:
        for customer, group in filtered.groupby("Customer"):
            st.markdown(f"### 👤 {customer}")
            for _, row in group.iterrows():
                st.markdown(f"**Message:** {row['Message']}")
                st.markdown(f"**Insight:** {row['AI Insight (raw)']}") 
                st.markdown(f"**Sentiment:** {row['Sentiment']}")
                st.markdown(f"**Suggested Action:** {row['Suggested Action']}")
                st.write("---")
    else:
        st.dataframe(filtered)

    # --- Download Insights ---
    csv_bytes = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Insights CSV", 
        csv_bytes, 
        "customer_chat_insights.csv", 
        "text/csv"
    )
