import os
from crewai import Task, Agent, Crew
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)


# Load environment variables
load_dotenv()

# Ensure LM Studio API URL and API key are set correctly
LM_STUDIO_URL = "http://localhost:1234/v1"  # LM Studio's API URL
LM_STUDIO_API_KEY = os.getenv("OPENAI_API_KEY")  # Default API key for LM Studio
MODEL_NAME ="lm_studio/meta-llama-3.1-8b-instruct"

# Initialize the default LLM (ChatOpenAI for LangChain compatibility)
default_llm = ChatOpenAI(
    openai_api_base=LM_STUDIO_URL,  # LM Studio's API URL
    openai_api_key=LM_STUDIO_API_KEY,  # API key for LM Studio
    model_name=MODEL_NAME,  # Ensure this matches your model name in LM Studio
    temperature=0.8,  # Adjust as needed
)

# Verify model availability
try:
    # Test a simple call to check model access
    response = default_llm.call({"prompt": "Test", "max_tokens": 5})
    logging.info(f"Model {MODEL_NAME} is available.")
except Exception as e:
    logging.error(f"Failed to access model {MODEL_NAME}: {str(e)}")

# Define the Market Analyst Agent
market_analyst = Agent(
    role="Senior Market Analyst",
    goal="Identify key market trends and opportunities for SaaS products that help in Task Management",
    backstory="You have good experience in analyzing tech markets and providing data-driven insights",
    verbose=True,
    llm=default_llm,
    allow_delegation=False,
    max_iter=2,
    max_execution_time=300,
)

# Define the Digital Marketing Strategist Agent
market_specialist = Agent(
    role="Digital Marketing Strategist",
    goal="Design a marketing campaign based on the analysis provided by the Market Analyst to drive awareness and adoption of our SaaS product. The product helps in Task Management using AI.",
    backstory="With a strong track record in Tech Marketing, you excel in creating high-impact digital strategies.",
    verbose=True,
    llm=default_llm,
    allow_delegation=True,
    max_iter=2,
    max_execution_time=300,
)

# Define tasks for the agents
task1 = Task(
    description="Conduct an in-depth analysis for a new Task Management SaaS product. Provide the answer in 10 bullet points, with a maximum of 300 words.",
    expected_output="A comprehensive market analysis report",
    agent=market_analyst,
)

task2 = Task(
    description="Using the market analysis report, develop a digital marketing strategy.",
    expected_output="A complete digital marketing plan for 3 months",
    agent=market_specialist,
)

# Execute the crew
crew = Crew(
    agents=[market_analyst, market_specialist],
    tasks=[task1, task2],
    verbose=True,
)

# Start the crew
try:
    results = crew.kickoff()
    print(results)

    # Save the result to a notepad file
    with open("output_result.txt", "w") as file:
        file.write(str(results))
except Exception as e:
    print(f"Error occurred: {str(e)}")

