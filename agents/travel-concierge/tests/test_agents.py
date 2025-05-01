import unittest
from google.adk.agents import Agent
from agents.travel_concierge.travel_concierge.root_agent import root_agent


class TestAgents(unittest.TestCase):
    def test_root_agent(self):
        new_root_agent = Agent(model="gemini-2.0-flash", name="new_root_agent", description="test")
        response = root_agent.execute("I want to book a trip to Madrid")
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()