from google.adk.agents import Agent

from travel_concierge.sub_agents.booking.agent import BookingAgent
from travel_concierge.sub_agents.inspiration.agent import inspiration_agent
from travel_concierge.sub_agents.planning.agent import planning_agent

booking_agent = BookingAgent(
    model="gemini-2.0-flash",
    name="booking_agent",
    description="Managing the booking process for tours, flights, and hotels",
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="The primary agent that coordinates all other sub-agents.",
    sub_agents=[inspiration_agent, planning_agent, booking_agent]
)