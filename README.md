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
```bash

LLM-Powered-Customer-Chat-Insight-Generator/
│
├── data/
    └── chat_insights_output
    └── sample_chats.csv
├── prompts/
    └── summarizer_prompts.txt
├── app.py                        # main app that generates the chat_insights
├── streamlit-app.py              # streamlit app code
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

```
## How to Run Locally

Clone this repo & run:

```bash
pip install -r requirements.txt
streamlit run app.py
```
## 📡 Deployment

This app is deployed on Streamlit Cloud. You can fork and redeploy your own version easily by:

1. Forking the repo
2. Visiting [Streamlit Cloud](https://share.streamlit.io)
3. Connecting to your GitHub repo
4. Setting the main file as `app.py`

## 💡 How It Works

The **AI Insight** column contains LLM-generated responses with 3 parts:

- **Customer Summary**
- **Sentiment** (e.g. Angry, Positive, Frustrated)
- **Suggested Action**

The app parses the **Sentiment** and enables filtering, grouping, and visualization to make sense of high-volume customer feedback.

## Skills Demonstrated

- **Prompt Engineering**
- **LLM Output Parsing**
- **Streamlit UI/UX**
- **Project Packaging for Deployment**
- **Workflow Automation**

## Screenshots

![App Demo](LLM-Powered-Customer-Chat-Insight-Generator/assest/giphy.mp4)



## 📬 Contact

Feel free to connect with me on [LinkedIn](www.linkedin.com/in/nomdorah-marcus-438262213)


I’d love feedback and collaboration!
