# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Inspiration agent. A pre-booking agent covering the ideation part of the trip."""

from google.adk.agents import Agent

from travel_concierge.sub_agents.inspiration import prompt
from travel_concierge.sub_agents.inspiration.place.agent import place_agent
from travel_concierge.sub_agents.inspiration.poi.agent import poi_agent
from travel_concierge.tools.places import map_tool


# Now place_agent and poi_agent are used as sub-agents, instead of been defined here.
inspiration_agent = Agent(
    model="gemini-2.0-flash",
    name="inspiration_agent",
    description="A travel inspiration agent who inspire users, and discover their next vacations; Provide information about places, activities, interests,",
    instruction=prompt.INSPIRATION_AGENT_INSTR,
    sub_agents=[place_agent, poi_agent],
    tools=[map_tool],
)
