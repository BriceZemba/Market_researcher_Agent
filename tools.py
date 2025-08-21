# tools.py
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ✅ Web Search Tool (Serper)
search_tool = SerperDevTool() 

# ✅ Web Scraper
scraper_tool = ScrapeWebsiteTool()