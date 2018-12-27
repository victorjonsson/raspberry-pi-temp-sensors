import tools
import json
import requests
from pprint import pprint

# Load configuration
config = tools.load_json_config()

# Setup gpio
tools.setup_gpio()

# Retreive temp data 
temperature_data = tools.read_temperatures(config)

# Send temp data to server
response = requests.post(
    config['server_api_url'],
    json = temperature_data,
    auth=(config['server_api_user'], config['server_api_password'])
);

# Send output to console
pprint(response)
print('Data pushed to server:')
print(json.dumps(temperature_data, indent=2, sort_keys=True))	
