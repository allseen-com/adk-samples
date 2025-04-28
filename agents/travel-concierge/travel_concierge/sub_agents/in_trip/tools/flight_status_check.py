import random
from typing import Any

from google.adk.tools import ToolContext


def flight_status_check(flight_number: str, flight_date: str) -> str:
    """
    Checks the status of a flight.

    Args:
        flight_number: The flight number (e.g., "AA123").
        flight_date: The flight date (e.g., "2024-07-20").

    Returns:
        A string describing the flight status.
    """
    statuses = ["on time", "delayed", "canceled"]
    status = random.choice(statuses)

    if status == "on time":
        return f"Flight {flight_number} on {flight_date} is on time."
    elif status == "delayed":
        delay_minutes = random.randint(15, 120)
        return f"Flight {flight_number} on {flight_date} is delayed by {delay_minutes} minutes."
    else:
        return f"Flight {flight_number} on {flight_date} is canceled."


def flight_status_check_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to check the status of a flight.

    Args:
        tool_context: The ADK tool context.
        **kwargs: Keyword arguments representing the inputs for flight_status_check.

    Returns:
        The flight status string.
    """

    flight_number = kwargs.get("flight_number")
    flight_date = kwargs.get("flight_date")

    if not all([flight_number, flight_date]):
        return "Missing required information for flight status check."

    return flight_status_check(flight_number, flight_date)