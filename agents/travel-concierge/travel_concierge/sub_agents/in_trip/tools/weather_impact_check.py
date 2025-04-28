import random
from typing import Any

from google.adk.tools import ToolContext


def weather_impact_check(location: str, date: str) -> str:
    """
    Checks the weather forecast for a location and date and determines potential impact.

    Args:
        location: The location (e.g., "Paris").
        date: The date (e.g., "2024-07-25").

    Returns:
        A string describing the weather and potential impact.
    """
    weather_conditions = [
        "clear skies",
        "partly cloudy",
        "light rain",
        "heavy rain",
        "snow",
        "thunderstorm",
    ]
    condition = random.choice(weather_conditions)

    if condition == "clear skies" or condition == "partly cloudy":
        impact = "no impact"
    elif condition == "light rain":
        impact = "allow extra travel time"
    elif condition == "heavy rain" or condition == "thunderstorm":
        impact = "allow significant extra travel time"
    else:  # snow
        impact = "consider rescheduling"

    return f"Weather forecast for {location} on {date}: {condition}. Potential impact: {impact}."


def weather_impact_check_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to check the weather forecast and potential impact.

    Args:
        tool_context: The ADK tool context.
        **kwargs: Keyword arguments representing the inputs for weather_impact_check.

    Returns:
        The weather forecast and impact string.
    """

    location = kwargs.get("location")
    date = kwargs.get("date")

    if not all([location, date]):
        return "Missing required information for weather impact check."

    return weather_impact_check(location, date)