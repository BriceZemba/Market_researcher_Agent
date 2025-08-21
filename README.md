
```markdown
# 🚀 Market Research CrewAI with Gemini 1.5 Flash

This project builds an **AI crew of specialized agents** that collect, analyze, and report on the latest market data.  
The crew leverages **CrewAI** for agent orchestration, **Google Gemini 1.5 Flash** as the LLM, and external tools like **Serper, NewsAPI, and web scrapers** to provide real-time insights.  


## 📊 Workflow Overview

1. **Data Collection Agent**  
   - Searches company websites, SEC filings, Yahoo Finance, Reddit, Twitter, and news sources.  
   - Uses tools: `SerperDevTool`, `ScrapeWebsiteTool`, `NewsAPIWrapper`, `WebResearchRetriever`.  

2. **Data Analyst Agent**  
   - Cleans and analyzes collected data using `pandas` and NLP techniques.  
   - Detects trends, risks, and sentiment.  
   - Powered by Gemini for reasoning.  

3. **Reporting Agent**  
   - Summarizes insights in natural, conversational language.  
   - Builds clean, presentation-ready reports with charts (`matplotlib`/`plotly`).  


## 📂 Project Structure

market\_researcher/
│── tools.py       # External tools (Serper, Scraper, NewsAPI, Retriever)
│── agents.py      # CrewAI agents (Collector, Analyst, Reporter) with Gemini LLM
│── tasks.py       # Tasks assigned to each agent
│── crew\.py        # Main entrypoint to run the crew
│── README.md      # Project documentation


## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/market_researcher.git
cd market_researcher
```bash

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 3. Install dependencies

```bash
pip install -r requirements.txt


### 4. Set API Keys

You’ll need API keys for:

* **Google Gemini** → `GOOGLE_API_KEY`
* **Serper** → `SERPER_API_KEY`
* **NewsAPI** → `NEWSAPI_API_KEY`

#### macOS/Linux:

```bash
export GOOGLE_API_KEY="your_gemini_key"
export SERPER_API_KEY="your_serper_key"
export NEWSAPI_API_KEY="your_newsapi_key"

#### Windows (PowerShell):

```powershell
setx GOOGLE_API_KEY "your_gemini_key"
setx SERPER_API_KEY "your_serper_key"
setx NEWSAPI_API_KEY "your_newsapi_key"


## 🚀 Running the Crew

```bash
python crew.py

The crew will:

1. Collect market data
2. Analyze trends & sentiment
3. Generate a clear report with charts

Output is displayed in the terminal, and reports can be extended to save as PDF/HTML.

---

## 📌 Example Output (simplified)

--- Final Report ---
📊 Market Update: AI Sector
- Positive sentiment on Reddit (76% bullish)
- SEC filings show increased R&D spending
- Yahoo Finance trend: steady 12% growth YoY
- Risks: high competition from startups

---

## 📜 License

MIT License. Free to use and modify.
```
