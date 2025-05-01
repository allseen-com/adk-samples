from google.adk.agents import Agent

from travel_concierge.sub_agents.planning import prompt
from travel_concierge.sub_agents.planning.itinerary.agent import itinerary_agent
from travel_concierge.sub_agents.inspiration.place.agent import place_agent
from travel_concierge.sub_agents.inspiration.poi.agent import poi_agent
from travel_concierge.tools.memory import get_user_preferences_tool


# This agent will have the itinerary_agent, the place_agent and the poi_agent
# as sub-agents and will use the get_user_preferences_tool.
planning_agent = Agent(
    model="gemini-2.0-flash",
    name="planning_agent",
    description="""Agent responsible for planning the trip""",
    instruction=prompt.PLANNING_AGENT_INSTR,
    sub_agents=[
        itinerary_agent,
        place_agent,
        poi_agent,
    ],  # This agent will use the itinerary_agent, the place_agent and the poi_agent
    tools=[get_user_preferences_tool],
)
