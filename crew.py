from crewai import Crew
from agents import property_researcher, property_analyst, old_property_researcher
from tasks import analysis_task,old_research_task, research_task

crew = Crew(
    agents=[old_property_researcher,property_analyst], 
    tasks=[research_task, analysis_task],
    verbose=True
    )

task_output = crew.kickoff()
print(task_output)
