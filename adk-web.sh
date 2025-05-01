#!/bin/bash

# Check if adk is installed
if ! command -v adk &> /dev/null
then
    echo "adk could not be found"
    exit
fi

echo "Starting adk web..."
# Start ADK Web
adk web

echo "ADK web has started. Keep this terminal open."

read -n 1 -s -r -p "Press any key to exit..."

echo "Exiting."