import tools
import json
import time
import os
import requests
from pprint import pprint

# change cwd to be able to run as cron job
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Load config
with open('./config.json') as f:
    config = json.load(f)

# Setup gpio
tools.setup_gpio()

# Retreive data and output to console
temperature_data = tools.read_temperatures(config)
response = requests.post(
    config['server_api_url'],
    json = temperature_data,
    auth=(config['server_api_user'], config['server_api_password'])
);
pprint(response)
print('Data pushed to server')
print(json.dumps(temperature_data, indent=2, sort_keys=True))	
