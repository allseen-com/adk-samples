"""Wrapper for search grounding."""

import random
from typing import Any

from google.adk.tools import ToolContext


def search(query: str, type: str) -> str:
    """
    Searches for information.

    Args:
        query: The query to search for.
        type: The type of data to search.

    Returns:
        A string with a list of results.
    """
    results = [
        f"Result 1: {query} - {type} - {random.randint(1,100)}",
        f"Result 2: {query} - {type} - {random.randint(1,100)}",
        f"Result 3: {query} - {type} - {random.randint(1,100)}",
    ]

    return "\n".join(results)


def search_tool(tool_context: ToolContext, **kwargs: Any) -> str:
    """
    Tool to search for information.

    Args:
        tool_context: The ADK tool context.
        **kwargs: Keyword arguments representing the inputs for search.

    Returns:
        The search results string.
    """
    query = kwargs.get("query")
    type = kwargs.get("type")

    if not all([query, type]):
        return "Missing required information for search."

    return search(query, type)
