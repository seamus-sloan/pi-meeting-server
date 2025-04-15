#!/bin/bash

# Exit on error
set -e

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start both scripts and save their PIDs
python server.py &
SERVER_PID=$!

python display_status.py &
DISPLAY_PID=$!

# Define cleanup function
cleanup() {
  echo "Shutting down..."
  kill $SERVER_PID $DISPLAY_PID
  wait
}

# Trap CTRL+C (SIGINT) and call cleanup
trap cleanup SIGINT

# Wait for both processes
wait