#!/bin/bash

# Exit on error
set -e

cd "$(dirname "$0")"

# Create venv only if it doesn't already exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# HACK: For some reason, my pi doesn't want to set the resolution correctly.
wlr-randr --output HDMI-A-1 --mode 848x480@60Hz

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