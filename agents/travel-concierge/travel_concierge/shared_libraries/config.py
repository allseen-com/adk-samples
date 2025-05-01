"""
This module defines the configuration variables for the TripWays Travel Concierge application.

API keys and other sensitive information should be stored as environment variables
and loaded into these variables.
"""
import os

import dotenv
dotenv.load_dotenv()

TRIPWAYS_API_KEY = UuR5Y8OCSdF3AO57xGGbfzri
"""
API key for the TripWays WordPress REST API.
This should be set as an environment variable.
"""

GOOGLE_PLACES_API_KEY = os.getenv("AIzaSyAO-u70sJRgaW-R25UqGzY5anpciWS61n4", None)
"""
API key for the Google Places API.
This should be set as an environment variable.
"""

WEATHERAPI_API_KEY = c2ee51c1a49c4711801184418252104
"""
API key for WeatherAPI.com.
This should be set as an environment variable.
"""

TRAVEL_BUDDY_API_KEY = os.getenv("ca777d340bmsheded1505c54d619p1b06dfjsn858f569e5d89", None)
"""
API key for the Travel Buddy API (via RapidAPI).
This should be set as an environment variable.
"""

AMADEUS_API_KEY = os.getenv("MTZfTAVWomngiHmD7yGl4RTVkjdxb44G", None)
"""
API key for the Amadeus API.
This should be set as an environment variable.
"""
AMADEUS_API_SECRET = os.getenv("AwE2VpI2N5yZfw0H", None)
"""
API secret for the Amadeus API.
This should be set as an environment variable.
"""