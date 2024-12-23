import os
import logging
from swarm import Swarm, Agent
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="agent1_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not set in the environment")

client = Swarm()

# Define agents
agent1 = Agent(
    name="RealEstateDemandAnalyst",
    instructions="Analyze residential and commercial real estate market demand, focusing on consumer preferences, economic factors, and location trends."
)
agent2 = Agent(
    name="PropertyDesignConsultant",
    instructions="Based on market demand, recommend features, amenities, and layouts for new properties in high-demand areas."
)
agent3 = Agent(
    name="ProjectCostEstimator",
    instructions="Calculate projected costs for property development, including land acquisition, construction, and materials, to ensure competitive pricing."
)
agent4 = Agent(
    name="SalesMarketingStrategist",
    instructions="Develop a marketing strategy for property listings, targeting specific demographics based on market trends and preferences."
)
agent5 = Agent(
    name="TenantRetentionSpecialist",
    instructions=" Suggest strategies for maintaining high tenant satisfaction and retention through effective communication, amenities, and property management."
)
# Message for agent1 to start
message1 = [{"role": "user", "content": "As the Real Estate Analyst, I need an analysis on residential and commercial real estate market demand, taking into consideration costumers preferences, demands and trends."}]

# Run agents with inter-agent communication
try:
    # Run agent 1
    response1 = client.run(agent=agent1, messages=message1)
    print("____________________________________________________________________________________________________________________________________________________________\n")
    print("RealEstateDemandAnalyst")
    print(response1)
    logging.info(f"Agent1 response - {response1}")

    # Prepare message for agent 2
    message2 = [
        {"role": "user", "content": f"Based on the Real Estate Demand Analyst: {response1}, what features, amenities and layouts should a new property have in high-demand areas?"}
    ]

    # Run agent 2
    response2 = client.run(agent=agent2, messages=message2)
    print("____________________________________________________________________________________________________________________________________________________________\n")
    print("PropertyDesignConsultant")
    print(response2)
    logging.info(f"Agent2 response - {response2}")

    # Prepare message for agent 3
    message3 = [
        {"role": "user", "content": f"Given the recommended features, amenities and layout: {response2}, develop a cost estimation plan applicable to acheiving this taking into account quality, eco-friendly materials at an affordable price."}
    ]

    # Run agent 3
    response3 = client.run(agent=agent3, messages=message3)
    print("____________________________________________________________________________________________________________________________________________________________\n")
    print("ProjectCostEstimator")
    print(response3)
    logging.info(f"Agent3 response - {response3}")
    
    
    # Prepare message for agent 4
    message4 = [
        {"role": "user", "content": f"Given the cost calculation and estimation in : {response3}, develop a Sales Marketing Strategy involving property listing for the demographic areas, preferences and trends."}
    ]

    # Run agent 4
    response4 = client.run(agent=agent4, messages=message4)
    print("____________________________________________________________________________________________________________________________________________________________\n")
    print("SalesMarketingStrategist")
    print(response4)
    logging.info(f"Agent4 response - {response4}")
    
    
     # Prepare message for agent 5
    message5 = [
        {"role": "user", "content": f"Given the market strategies based on customer preferences, trends  in : {response4}, develop a Strategy that should be implemented to retain customers satisfaction based on the services provided."}
    ]

    # Run agent 5
    response5 = client.run(agent=agent5, messages=message5)
    print("____________________________________________________________________________________________________________________________________________________________\n")
    print("TenantRetentionSpecialist")
    print(response5)
    logging.info(f"Agent4 response - {response5}")



except Exception as e:
    print(f"An error has occurred: {e}")
    logging.exception("An error occurred")


# def execute_agent(agent, messages, agent_name):
#     try:
#         response = client.run(agent=agent, messages=messages)
#         print(f"____________________________________________________________________________________________________\n{agent_name}")
#         print(response)
#         logging.info(f"{agent_name} response - {response}")
#         return response
#     except Exception as e:
#         print(f"Error with {agent_name}: {e}")
#         logging.exception(f"{agent_name} encountered an error")
#         raise

# # Execute Agents
# try:
#     response1 = execute_agent(agent1, message1, "RealEstateDemandAnalyst")
#     message2 = [{"role": "user", "content": f"Based on the Real Estate Demand Analyst: {response1}..."}]
#     response2 = execute_agent(agent2, message2, "PropertyDesignConsultant")
#     message3 = [{"role": "user", "content": f"Given the recommended features: {response2}..."}]
#     response3 = execute_agent(agent3, message3, "ProjectCostEstimator")
#     message4 = [{"role": "user", "content": f"Given the cost estimation: {response3}..."}]
#     response4 = execute_agent(agent4, message4, "SalesMarketingStrategist")
#     message5 = [{"role": "user", "content": f"Given the marketing strategy: {response4}..."}]
#     response5 = execute_agent(agent5, message5, "TenantRetentionSpecialist")
# except Exception as e:
#     print(f"An error occurred: {e}")
