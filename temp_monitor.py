import os
import glob
import time
import json

# Setup gpio
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Load configuration from json
with open('./config.json') as f:
    config = json.load(f)

# Method used to load data from all devices
def get_sensors():
    sensors = [];
    for device in config['devices']:
        f = open(config['devices_base_dir'] + device['folder'] + '/w1_slave')
        sensors.append({
            'name': device['name'], 
            'lines': f.readlines()
        })
        f.close()
    return sensors

# Method used to get a dict with each sensor and the read celsius degree 
def read_temperatures():
    temps = {}
    sensors = get_sensors()
    for sensor in sensors:
        if sensor['lines'][0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            return read_temperatures()
        equals_pos = sensor['lines'][1].find('t=')
        if equals_pos != -1:
            temp_string = sensor['lines'][1][equals_pos+2:]
            celsius = float(temp_string) / 1000.0
            # FARENHEIT = temp_c * 9.0 / 5.0 + 32.0
            temps[sensor['name']] = round(celsius, 1)
    return temps

# Output data from all sensors
while True:
    print(json.dumps(read_temperatures(), indent=2, sort_keys=True))	
    time.sleep(1)
