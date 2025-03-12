from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent=Agent(
    name='web_agent',
    role='search the web for information',
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources of the information you provide",
    show_tool_calls=True,
    markdown=True,
)

finance_agent=Agent(
    name='Finance_agent',
    role='Get financial data',
    model=OpenAIChat(id="gpt-4o mini"),
    tools=[YFinanceTools()],
    instructions="Use tables to display the data",
    show_tool_calls=True,
    markdown=True,
)

agent_team=Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include the sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Analyze companies like Tesla, Apple, and Google to buy for long term investment")