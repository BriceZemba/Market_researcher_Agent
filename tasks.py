# tasks.py
from crewai import Task
from agents import data_collector, data_analyst, reporting_agent

# Task 1: Collect Data
collect_data_task = Task(
    description="Search company websites, SEC filings, Yahoo Finance, Reddit, and Twitter for the latest market data.",
    expected_output="A structured dataset of financials, company updates, and social sentiment.",
    agent=data_collector
)

# Task 2: Analyze Data
analyze_data_task = Task(
    description="Clean and analyze the collected data using pandas. Apply statistical models and NLP to find trends and sentiment.",
    expected_output="A structured analysis with key trends, risks, and opportunities.",
    agent=data_analyst
)

# Task 3: Generate Report
report_task = Task(
    description="Turn the analysis into a clear, visual report with charts and natural-language summaries.",
    expected_output="A presentation-ready report summarizing findings with charts and highlights.",
    agent=reporting_agent
)
