from google.adk.agents import Agent
from travel_concierge.sub_agents.planning import prompt


itinerary_agent = Agent(
    model="gemini-2.0-flash",
    name="itinerary_agent",
    description="Agent responsible for creating the detailed travel itinerary.",
    instruction=prompt.ITINERARY_AGENT_INSTR
)