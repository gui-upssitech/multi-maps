# Multi-maps

Small python application as a proof-of-concept for muti-modal fusion for human-to-robot interaction.

The app shows a mapof a city with multiple points of interest (POI). The user can ask for directions by :
1. specifying a starting point on the map using a pointer (mouse, eyetracker, etc.)
2. specifying a destination using speech 


## Installation

1. On Ubuntu, install `portaudio` for the voice recognition to work

```bash
sudo apt install portaudio19-dev -y
```

2. Create a Python 3.10 environment (conda, venv, or other)
3. Install project dependencies

```bash
pip install -U pip
pip install -r ./requirements.txt
```

## Run the app

Source the python environment then

```bash
python src/main.py
```
