from typing import Any, Dict
from abc import ABC
from travel_concierge.shared_libraries import config

class Agent(ABC):
    """Abstract base class for agents."""

    def __init__(self, name: str, description: str) -> None:
        """Initializes the agent with a name and description.

        Args:
            name: The name of the agent.
            description: A description of the agent's purpose.
        """
        self.name = name
        self.description = description

    def run(self, prompt: str, **kwargs: Any) -> Any:  # type: ignore
        """Runs the agent with the given prompt and keyword arguments.

        Args:
            prompt: The prompt to run the agent with.
            **kwargs: Keyword arguments to pass to the agent.

        Returns:
            The result of running the agent.
        """
        raise NotImplementedError

class BookingAgent(Agent):
    """
    Agent responsible for managing the booking process for tours, flights, and hotels.
    """
    def __init__(self, name: str = "booking_agent", description: str = "Agent for managing the booking process for tours, flights, and hotels."):
        super().__init__(name, description)
        print(f"TRIPWAYS_API_KEY: {config.TRIPWAYS_API_KEY}")

    def check_availability(self, request: Dict) -> str:
        """
        Verifies the availability of the requested service (tour, hotel, etc.).
        Args:
            request: A dictionary containing the request details.
        Returns:
            A string indicating that the check_availability function was executed.
        """
        function_name = "check_availability"
        return f"{self.name}: {function_name}"

    def retrieve_details(self, request: Dict) -> str:
        """
        Fetches detailed information about the selected service.
        Args:
            request: A dictionary containing the request details.
        Returns:
            A string indicating that the retrieve_details function was executed.
        """
        function_name = "retrieve_details"
        return f"{self.name}: {function_name}"

    def user_confirmation(self, request: Dict) -> str:
        """
        Presents the details to the user and requests confirmation.
        Args:
            request: A dictionary containing the request details.
        Returns:
            A string indicating that the user_confirmation function was executed.
        """
        function_name = "user_confirmation"
        return f"{self.name}: {function_name}"

    def collect_user_information(self, request: Dict) -> str:
        return "collect_user_information"

    def payment_choice(self, request: Dict) -> str:
        return "payment_choice"

    def secure_payment(self, request: Dict) -> str:
        return "secure_payment"

    def confirm_booking(self, request: Dict) -> str:
        return "confirm_booking"

    def generate_booking_id(self, request: Dict) -> str:
        return "generate_booking_id"

    def store_booking_details(self, request: Dict) -> str:
        return "store_booking_details"

    def notify_user(self, request: Dict) -> str:
        return "notify_user"