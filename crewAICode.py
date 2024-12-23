import os
import openai
from crewai import Task, Agent, Crew, Process
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv, find_dotenv


load_dotenv()

# default_llm = OpenAI(base_url="", api_key="lm-studio")

#DEFINE THE LANGUAGE MODEL
# default_llm = ChatOpenAI(
#     openai_api_key=os.getenv("OPENAI_API_KEY"),
#     model="hugging-quants/llama-3.2-1b-instruct-q8_0.gguf",
#     temperature=0.8
# )

default_llm = ChatOpenAI(
openai_api_base ="http://localhost:1234/v1",
openai_api_key = os.getenv("OPENAI_API_KEY"),
model_name = "lm_studio/meta-llama-3.1-8b-instruct"


)
# http://localhost:1234/v1

#lm_studio/Llama 3.1 8B
#Meta-Llama-3.1-8B-Instruct-GGUF


market_analyst = Agent(
    role="Senior Market Analyst",
    goal="Identify key market trends and opportunities for saas products that help in Task Management",
    backstory="You have good experience in analysing tech markets and providing data-driven Insights",
    verbose=True,  # Default: False
    llm=default_llm,  # Default: OPENAI_MODEL_NAME or "gpt-4"
    allow_delegation=False,  # Default: False
    max_iter=2,  # Default: 20 iterations
    max_execution_time=300,  # Optional: Maximum execution time in seconds
    
)

market_specialist = Agent(
    role="Digital Marketing Strategist",
    goal="Design a mrketing campaign you got from market analyst to drive awareness and adoption of our saas product. Our product helps in Task Management using AI",
    backstory="With a strong track record in Tech Marketing you excel in creating high-impact digital strategies",
    verbose=True,  # Default: False
    llm=default_llm,  # Default: OPENAI_MODEL_NAME or "gpt-4"
    allow_delegation=True,  # Default: False
    max_iter=2,  # Default: 20 iterations
    max_execution_time=300,  # Optional: Maximum execution time in seconds
    
)

#Define task for Agents

task1 = Task(
    description='Conduct an in-depth analysis for a new Task Management Saas product. Give the answer in 10 bullet points and maximum of 300 words',
    expected_output='A comprehensive market analysis report',
    agent=market_analyst,
)


task2 = Task(
    description='Using the market analysis report, develop a digital marketing strategy',
    expected_output='A complete digital marketing plan for 3 months',
    agent=market_specialist,
)

# Execute the crew

crew = Crew(
    agents=[market_analyst, market_specialist],
    tasks=[task1, task2],
    verbose=True
)

# Start the crew

try:
    results = crew.kickoff()
    print(results)
except Exception as e:
    print(f"Error occurred: {str(e)}")


# save the result to a notepad file

# with open("output_result.txt", "w") as file:
#     file.write(str(results))