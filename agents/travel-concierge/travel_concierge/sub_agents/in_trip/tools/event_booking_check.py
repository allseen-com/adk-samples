import random
from typing import Any

from google.adk.tools import ToolContext


def event_booking_check(event_name: str, event_date: str, event_location:str) -> str:
    """
    Checks the booking status of an event.

    Args:
        event_name: The name of the event.
        event_date: The date of the event.
        event_location: the location of the event

    Returns:
        A string describing the event booking status.
    """
    statuses = ["confirmed", "canceled", "postponed"]
    status = random.choice(statuses)

    if status == "confirmed":
        return f"The booking for {event_name} on {event_date} at {event_location} is confirmed."
    elif status == "canceled":
        return f"The booking for {event_name} on {event_date} at {event_location} has been canceled."
    else:
        new_date = "2024-08-15"  # Example new date for simulation
        return f"The event {event_name} on {event_date} at {event_location} has been postponed. New date: {new_date}."


def event_booking_check_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to check the booking status of an event.

    Args:
        tool_context: The ADK tool context.
        **kwargs: Keyword arguments representing the inputs for event_booking_check.

    Returns:
        The event booking status string.
    """

    event_name = kwargs.get("event_name")
    event_date = kwargs.get("event_date")
    event_location = kwargs.get("event_location")

    if not all([event_name, event_date, event_location]):
        return "Missing required information for event booking check."

    return event_booking_check(event_name, event_date, event_location)