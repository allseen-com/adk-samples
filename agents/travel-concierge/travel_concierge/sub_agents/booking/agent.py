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

"""Booking agent and sub-agents, handling the confirmation and payment of bookable events."""

from google.adk.agents import Agent
from travel_concierge.sub_agents.booking.confirm_reservation.agent import (
    confirm_reservation_agent,
)
from travel_concierge.sub_agents.booking.payment.agent import payment_agent
from travel_concierge.sub_agents.booking.payment_choice.agent import (
    payment_choice_agent,
)



booking_agent = Agent(
    model="gemini-2.0-flash",
    name="booking_agent",
    description="Agent responsible for managing the booking process.",    sub_agents=[
        confirm_reservation_agent,
        payment_choice_agent,
        payment_agent,
    ],
)
