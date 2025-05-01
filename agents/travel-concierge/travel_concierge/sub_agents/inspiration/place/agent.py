from google.adk.agents import Agent

from travel_concierge.tools.search import search_tool


place_agent = Agent(
    model="gemini-2.0-flash",
    name="place_agent",
    description="Agent responsible for searching places and its related information.",
    tools=[search_tool],
)