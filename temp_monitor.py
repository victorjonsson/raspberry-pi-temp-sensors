import tools
import json
import time

# Load config
config = tools.load_json_config()

# Setup gpio
tools.setup_gpio()

# Retreive data and output to console
while True:
    temperature_data = tools.read_temperatures(config)
    print(json.dumps(temperature_data, indent=2, sort_keys=True))	
    time.sleep(1)
