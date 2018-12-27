import os
import glob
import time
import json

# Get config josn
def load_json_config():
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file_path = current_dir_path + '/config.json'
    with open(config_file_path) as f:
        config = json.load(f)
    return config

# Setup gpio
def setup_gpio():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

# Method used to load data from all devices
def get_sensors(config):
    sensors = [];
    for device in config['sensors']:
        f = open(config['sensors_base_dir'] + device['folder'] + '/w1_slave')
        sensors.append({
            'name': device['name'], 
            'lines': f.readlines()
        })
        f.close()
    return sensors

# Method used to get a dict with each sensor and the read celsius degree 
def read_temperatures(config):
    temps = {}
    sensors = get_sensors(config)
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


