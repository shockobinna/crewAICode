import os
import logging
from swarm import Swarm, Agent
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="agent_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not set in the environment")

client = Swarm()

# Define agents
agent1 = Agent(
    name="MarketTrendsAnalyst",
    instructions="Analyze current trends in the US automobile industry, focusing on consumer preferences, emerging technologies, and competitors' offerings."
)
agent2 = Agent(
    name="ProductDevelopmentConsultant",
    instructions="Based on the market trends, recommend features, specifications, and design elements for the new car model that will appeal to US consumers."
)
agent3 = Agent(
    name="LaunchStrategyAdvisor",
    instructions="Develop a launch strategy for the new car model considering the recommended features and current market conditions."
)

# Message for agent1 to start
message1 = [{"role": "user", "content": "As the CEO, I need an analysis of the current US automobile market trends to get information on our new car model development."}]

# Run agents with inter-agent communication
try:
    # Run agent 1
    response1 = client.run(agent=agent1, messages=message1)
    print("MarketTrendsAnalyst")
    print(response1)
    logging.info(f"Agent1 response - {response1}")

    # Prepare message for agent 2
    message2 = [
        {"role": "user", "content": f"Based on the market trend analysis: {response1}, what features and specifications should our new car model have to succeed in the US car market?"}
    ]

    # Run agent 2
    response2 = client.run(agent=agent2, messages=message2)
    print("ProductDevelopmentConsultant")
    print(response2)
    logging.info(f"Agent2 response - {response2}")

    # Prepare message for agent 3
    message3 = [
        {"role": "user", "content": f"Given the recommended features and specifications: {response2}, develop a launch strategy for the US car market."}
    ]

    # Run agent 3
    response3 = client.run(agent=agent3, messages=message3)
    print("LaunchStrategyAdvisor")
    print(response3)
    logging.info(f"Agent3 response - {response3}")

except Exception as e:
    print(f"An error has occurred: {e}")
    logging.exception("An error occurred")
