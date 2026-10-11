import google.auth 

from google.adk.agents.llm_agent import Agent
from team.agents.finance_agent.tools import describe_file, query_file
from team.agents.finance_agent.prompt import SYSTEM_PROMPT

_, PROJECT = google.auth.default()

financeagent = Agent(
    model='gemini-3.8-flash',
    name='financeagent',
    description='Ayuda a realizar analisis financiero avanzado',
    instruction=SYSTEM_PROMPT,
    tools=[describe_file, query_file]
)