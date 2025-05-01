from google.adk.agents import Agent

from travel_concierge.tools.search import search_tool


poi_agent = Agent(
    model="gemini-2.0-flash",
    name="poi_agent",
    description="Agent responsible for searching points of interest and its related information.",
    tools=[search_tool],
)