from google.adk.agents import Agent
from travel_concierge.sub_agents.booking import prompt


payment_agent = Agent(
    model="gemini-2.0-flash",
    name="payment_agent",
    description="Agent responsible for managing the payment process and interacting with payment gateways.",
    instruction=prompt.PAYMENT_AGENT_INSTR,
)