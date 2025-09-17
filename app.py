import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ No API key found. Please set OPENAI_API_KEY in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_insight(chat_text):
    """Send customer chat text to GPT and return structured insight."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Or "gpt-4o", "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an assistant that extracts insights from customer chats."},
                {"role": "user", "content": f"Analyze this chat:\n{Message}\n\nReturn a summary, sentiment, and action items."}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ API Error: {e}"

def process_chats(input_csv, output_csv):
    """Read customer chats from CSV, process with GPT, and save insights."""
    df = pd.read_csv(input_csv)

    if "chat_text" not in df.columns:
        raise ValueError("❌ Input CSV must have a 'chat_text' column.")

    insights = []
    for i, row in df.iterrows():
        chat = row["Message"]
        insight = generate_insight(chat)
        insights.append(insight)
        print(f"[{i+1}/{len(df)}] Processed: {chat[:50]}...")

    df["insight"] = insights
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved {len(df)} insights to {output_csv}")

if __name__ == "__main__":
    process_chats("data/sample_chats.csv", "data/chat_insights_output.csv")
