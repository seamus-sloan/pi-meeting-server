
# Pi Meeting Screen

This is a small Flask server that will update your meeting status to be displayed on a screen attached to the pi.

## Requirements

Python, pip, a Raspberry Pi, a screen for the pi.

## Running

```sh
# Checkout the repo & navigate to the directory
git clone https://github.com/seamus-sloan/pi-meeting-server.git
cd pi-meeting-server

# Set your venv
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the programs
python server.py & python display_status.py 
```
