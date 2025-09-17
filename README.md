# AI-Powered Customer Chat Analysis
**Upload your customer chat data → Get insights in seconds.**  

AI-Powered Customer Chat Analysis is a **Streamlit web app** that uses **OpenAI GPT models** to analyze customer conversations.  
It automatically generates:  
- **Customer summaries** – short and clear recaps of what the customer is saying  
- **Sentiment scores** – detect if the message is Positive, Neutral, or Negative  
- **Suggested actions** – recommended next steps for customer support or sales teams  

This project is part of my **data science portfolio** and demonstrates how AI can turn raw customer chats into **business-ready insights**.  

## Why this project? ##

Businesses deal with hundreds of customer chats daily. Manually reviewing them is time-consuming and messy.
- This app shows how AI can help:

- Save time by summarizing conversations automatically

- Spot unhappy customers faster with sentiment detection

- Suggest smart next steps for better customer service

---

## Demo Flow  
1. Upload a CSV file with `Customer` and `Message` columns.  
2. The AI processes each chat message.  
3. Instantly get summaries, sentiment distribution, and suggested actions.  
4. Filter insights, group by customer, and download results as CSV.  

---

## Features  
- File upload (CSV format)  
- AI-powered text analysis (OpenAI GPT models)  
- Sentiment distribution chart (positive/neutral/negative %)  
- Detailed insights (with filtering + grouping by customer)  
- Export insights as CSV  
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

1. Clone this repo & run:
```bash
git clone https://github.com/SharonE-coder/LLM-Powered-Chat-Analysis.git
cd LLM-Powered-Chat-Analysis
```
2. Create a virtual environment
```
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key

Create a .env file in the project root and add:
```
OPENAI_API_KEY=your_api_key_here
```

Run the App
```
streamlit run streamlit-app.py
```
Then open the local URL that Streamlit provides (usually http://localhost:8501).

Author

Nomdorah Marcus & Oluwafemi Oloye
LinkedIn: [LinkedIn](https://www.linkedin.com/in/nomdorah-marcus-438262213/)
GitHub: [Your GitHub](https://github.com/SharonE-coder)

⭐ If you like this project, don’t forget to star the repo!
I’d love feedback and collaboration!
