# crew.py
from crewai import Crew
from agents import data_collector, data_analyst, reporting_agent
from tasks import collect_data_task, analyze_data_task, report_task

# Create the crew
crew = Crew(
    agents=[data_collector, data_analyst, reporting_agent],
    tasks=[collect_data_task, analyze_data_task, report_task],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n--- Final Report ---")
    print(result)
