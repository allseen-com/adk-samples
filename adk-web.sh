#!/bin/bash

# Activate the environment
echo "Activating environment..."
if ! command -v direnv &> /dev/null
then
    echo "direnv could not be found"
    exit
fi

if [ -f .envrc ]; then
    direnv allow
else
    echo ".envrc not found"
    exit
fi

# Navigate to the correct directory (if needed)
# cd /path/to/your/project

echo "Starting adk web..."

# Start ADK Web
if ! command -v adk &> /dev/null
then
    echo "adk could not be found"
    exit
fi
adk web

echo "ADK web has started. Keep this terminal open."

read -n 1 -s -r -p "Press any key to exit..."

echo "Exiting."
# Start ADK Web
adk web

echo "ADK web has started. Keep this terminal open."

read -n 1 -s -r -p "Press any key to exit..."

echo "Exiting."