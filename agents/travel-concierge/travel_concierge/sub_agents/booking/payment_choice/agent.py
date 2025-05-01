from google.adk.agents import Agent
from travel_concierge.sub_agents.booking import prompt


payment_choice_agent = Agent(
    model="gemini-2.0-flash",
    name="payment_choice_agent",
    description="Agent responsible for providing payment options and helping the user choose the right one.",
    instruction=prompt.PAYMENT_CHOICE_AGENT_INSTR,
)