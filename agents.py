# agents.py
from crewai import Agent
from tools import search_tool, scraper_tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# ✅ Use Gemini 1.5 Flash as the LLM
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini/gemini-1.5-flash",
    temperature=0.3, 
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Data Collection Agent
data_collector = Agent(
    role="Market Data Collector",
    goal="Collect the most up-to-date financial, company, and social media data.",
    backstory="An expert in sourcing real-time data from trusted financial, regulatory, and social platforms.",
    tools=[search_tool, scraper_tool],
    llm=gemini_llm,
    verbose=True
)

# Data Analyst Agent
data_analyst = Agent(
    role="Data Analyst",
    goal="Clean, structure, and analyze financial and sentiment data for hidden insights.",
    backstory="A sharp data scientist skilled with pandas, statistics, and NLP for trend detection.",
    tools=[],
    llm=gemini_llm,
    verbose=True
)

# Reporting Agent
reporting_agent = Agent(
    role="Reporting Specialist",
    goal="Turn complex insights into clear, visually compelling reports.",
    backstory="A storytelling analyst who builds clean visuals and writes human-friendly summaries.",
    tools=[],
    llm=gemini_llm,
    verbose=True
)
