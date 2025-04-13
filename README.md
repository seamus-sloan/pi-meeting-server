
# Pi Meeting Screen

A lightweight Flask + Pygame project to display meeting status information on a screen. Designed to run on a Raspberry Pi with a screen attached, but can also run on Windows for testing or development.

## Features

- REST API server to GET/POST meeting status
- Visual display of status using Pygame
- Automatically polls the server to show real-time updates
- Can show fullscreen on Pi, or windowed for debugging

## Requirements

- Python 3.9+
- `pip`, `venv`
- Required packages listed in `requirements.txt`

## Setup Instructions

### 🪟 Running on Windows

```sh
# Clone the repo
git clone https://github.com/yourusername/pi-meeting-server.git
cd pi-meeting-server

# Create & activate venv
python -m venv venv
venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py

# Run the display (DEBUG for windowed mode)
$env:DEBUG="true"
python display_status.py
```

### 🍓Running on Pi

```sh
# Clone the repo
git clone https://github.com/yourusername/pi-meeting-server.git
cd pi-meeting-server

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the scripts
python server.py & python display_status.py
```
