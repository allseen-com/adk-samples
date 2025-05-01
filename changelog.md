# Changelog

## Today

- **Corrected Nix Environment**: 
    *   Refactored `dev.nix` to use `pkgs.mkShell` correctly, resolving infinite recursion and environment build failures. Updated `default.nix` to correctly call `dev.nix`. This improvement ensures a clean, reproducible, and efficient development environment setup, enabling faster and more reliable environment creation.


-   Add the get_time function to the PlacesService class in places.py.
-   Create the transit_coordination_tool in transit_coordination.py and update the day_of_agent to use this tool.
-   Create the flight_status_check_tool in flight_status_check.py and update the trip_monitor_agent to use this tool.
-   Create the event_booking_check_tool in event_booking_check.py and update the trip_monitor_agent to use this tool.
-   Create the weather_impact_check_tool in weather_impact_check.py and update the trip_monitor_agent to use this tool.
- Create the search_tool in search.py.
- Create the place_agent.
- Create the poi_agent.
- Update the inspiration_agent to use those agents and create the root_agent to use the inspiration_agent.
- Create the memory module in memory.py to store user preferences and make the in_trip_agent use the memory_tool and get_user_preferences_tool.
- Create the planning_agent.
- Create the itinerary_agent.
- Update the root_agent to use those agents.
- Create the booking_agent.
- Create the confirm_reservation_agent.
- Create the payment_choice_agent.
- Create the payment_agent.
- Update the root_agent to use the booking_agent.
