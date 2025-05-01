from google.adk.agents import Agent
from travel_concierge.sub_agents.booking import prompt


confirm_reservation_agent = Agent(
    model="gemini-2.0-flash",
    name="confirm_reservation_agent",
    description="Agent responsible for confirming the reservation details with the user before finalizing the booking.",
    instruction=prompt.CONFIRM_RESERVATION_AGENT_INSTR,
)