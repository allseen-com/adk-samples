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

"""Transit coordination tool for in-trip agent."""

from datetime import datetime, timedelta
from typing import Any

from google.adk.tools import ToolContext

def transit_coordination(
    travel_from: str,
    leave_by_time: str,
    travel_to: str,
    arrive_by_time: str,
    current_time: str,
) -> str:
    """
    Provides transit coordination suggestions based on travel details.

    Args:
        travel_from: The starting location.
        leave_by_time: The latest time to leave.
        travel_to: The destination location.
        arrive_by_time: The desired arrival time.
        current_time: The current time.

    Returns:
        A string containing the transit suggestion.
    """
    current_datetime = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

    if travel_from == travel_to:
        return "You are already at your destination. There is nothing to do."

    try:
        arrive_by_datetime = datetime.strptime(arrive_by_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        arrive_by_datetime = None

    if arrive_by_datetime is not None and (arrive_by_datetime - current_datetime) > timedelta(hours=2):
        return "Your arrival time is in the future. There is nothing to do just yet."

    if arrive_by_time == "as soon as possible" or (arrive_by_datetime is not None and arrive_by_datetime <= (current_datetime + timedelta(hours=2))):
        if "airport" in travel_to.lower():
            buffer_time = timedelta(hours=2)
            transportation_mode = "taxi"
            suggestion = f"You are traveling to {travel_to} which is an airport. I suggest you take a {transportation_mode} and leave by {(current_datetime + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')} to account for security checks."
        else:
            transportation_mode = "Uber"
            eta = "20 minutes"
            pickup_point = "the main entrance"
            suggestion = f"You can take an {transportation_mode} to reach {travel_to}. The ETA is approximately {eta}. You can get picked up at {pickup_point}. I suggest you leave now."
        return suggestion
    
    return "I cannot process your request"


def transit_coordination_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to provide transit coordination suggestions.

    Args:
        tool_context: The ADK tool context.
        **kwargs: Keyword arguments representing the inputs for transit_coordination.

    Returns:
        The transit suggestion string.
    """
    
    travel_from = kwargs.get("travel_from")
    leave_by_time = kwargs.get("leave_by_time")
    travel_to = kwargs.get("travel_to")
    arrive_by_time = kwargs.get("arrive_by_time")
    current_time = tool_context.get("_time")

    if not all([travel_from, leave_by_time, travel_to, arrive_by_time, current_time]):
        return "Missing required information for transit coordination."

    return transit_coordination(travel_from, leave_by_time, travel_to, arrive_by_time, current_time)