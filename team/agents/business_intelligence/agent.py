import google.auth 

from google.adk.agents.llm_agent import Agent
from team.agents.business_intelligence.tools import describe_file, query_file
from team.agents.business_intelligence.prompt import SYSTEM_PROMPT

_, PROJECT = google.auth.default()


biagent = Agent(
    model='gemini-3.8-flash',
    name='biagent',
    description='Ayuda a realizar analisis avanzado de datos',
    instruction=SYSTEM_PROMPT,
    tools=[describe_file, query_file],
)