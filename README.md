# LLM-Powered Customer Chat Analysis

This is a Streamlit dashboard that transforms raw customer conversations into **clean summaries, sentiment scores, and actionable insights** using GPT.  

This project demonstrates:
- **Prompt engineering** for structured LLM outputs  
- **LLM output parsing** and workflow automation  
- **Data exploration & visualization** in Streamlit  

🔗 **[Live Demo](https://llm-powered-customer-chat-insight-generatorgit-jegqhfuwed2gnv4.streamlit.app/)**  

---

## Features
- Upload customer chat CSVs (AI-enhanced or raw logs)  
- Filter conversations by sentiment (Satisfied, Angry, Frustrated, etc.)  
- Keyword search across messages & insights  
- Group chats by customer for deeper analysis  
- Visualize sentiment distribution with bar charts  
- Export filtered results for reporting  


---

## Example Use Cases
- Customer complaint tracking  
- Support conversation summarization  
- CX (Customer Experience) trend analysis  
- AI prompt engineering showcase  

---

## Input Format
The app expects a CSV with the following columns:  

| Customer | Message | AI Insight |
|----------|---------|------------|
| John Doe | Hi, my internet hasn't worked for two days. I'm frustrated. | **Customer Summary:** Internet not working… **Sentiment:** Frustrated. **Suggested Action:** Troubleshoot. |

---

## Project Structure

LLM-Powered-Customer-Chat-Insight-Generator/
│
├── data/
│ ├── chat_insights_output.csv
│ └── sample_chats.csv
├── prompts/
│ └── summarizer_prompts.txt
├── app.py # Generates AI chat insights
├── streamlit-app.py # Streamlit dashboard
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## Run Locally
Clone the repo & install dependencies:
```bash
pip install -r requirements.txt
streamlit run app.py

Deployment

This app is deployed on Streamlit Cloud.
You can fork & redeploy your own version in 3 steps:

Fork the repo

Link it to Streamlit Cloud

Set the main file to app.py

💡 How It Works

The AI Insight column contains structured GPT outputs with three parts:

Customer Summary

Sentiment (e.g., Positive, Angry, Frustrated)

Suggested Action

The Streamlit dashboard provides these outputs, enabling filtering, grouping, and visualization to quickly uncover insights from large volumes of chats.

Skills Demonstrated

Prompt Engineering

LLM Output Parsing & Data Wrangling

Interactive Dashboards with Streamlit

Project Packaging & Deployment

Workflow Automation

Screenshots

(Add screenshots or GIFs of your dashboard here to make the repo more engaging!)

📬 Contact

I’d love feedback and collaboration!