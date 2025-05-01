from typing import Any
from google.adk.tools import ToolContext

# In-memory dictionary to simulate a database
user_data = {}


def memorize(user: str, data: dict) -> str:
    """
    Memorizes (stores) user data in the simulated database.

    Args:
        user: The user identifier (e.g., user's name or ID).
        data: A dictionary containing the data to store for the user.

    Returns:
        A string indicating the status of the operation.
    """
    if user not in user_data:
        user_data[user] = {}
    user_data[user].update(data)
    return f"Data memorized for user {user}."


def get_user_preferences(user: str) -> str:
    """
    Retrieves user preferences from the simulated database.

    Args:
        user: The user identifier.

    Returns:
        A string with the user preferences.
    """
    if user in user_data:
        return str(user_data[user])
    else:
        return f"No preferences found for user {user}."


def memorize_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to memorize (store) user data.

    Args:
        **kwargs: Keyword arguments representing the inputs for memorize.

    Returns:
        The string indicating the status of the operation.
    """
    user = kwargs.get("user")
    data = kwargs.get("data")
    if not all([user, data]):
        return "Missing required information for memorize."
    return memorize(user, data)
    
def get_user_preferences_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to get user data.
    """
    user = kwargs.get("user")
    if not all([user]):
        return "Missing required information for get_user_preferences."
    return get_user_preferences(user)
