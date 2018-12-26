# Raspberry Pi Temperature Sensors

How to setup a raspberry pi with multiple DS18B20 (temperature) sensors.

---

## Prerequisites

- Raspberry pi 3
- Micro SD-card
- 1 (or more) DS18B20 temperature sensors
- 1 breakout board (so you won't have to fiddle with a resistor and bread board)
- Jumper cables (female <-> female)

## Tutorial

This is my personal setup. There's probably tons of different ways to get this done but here you have my take on it:

### 1) Initial setup of the raspberry pi
Follow the [instructions on how to setup a headless raspberry pi](https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0).

### 2) Connecto temperature sensors
Connect your sensors to the raspberry pi following this youtube instruction:  https://www.youtube.com/watch?v=j7LLVkPpQ78 . **Notice** that DS18B20 sensors uses the "Dallas 1-Wire protocol" which means that you can connect multiple sensors in parallel.

### 3) Download the python scripts
Having completed the step above you should be able to get data from the sensors. Now you can download the scripts in this repository and place them somewhere suitable on your raspberry pi. You can do this by installing git on the pi, or simply by doing some "cut and paste" if that is your taste.

### 4) Configure 
Open the file `config.json` and add the folders and names of each sensor you have connected to the pi. You can choose any name you want for each sensor, you find the folder of each sensor in `/sys/bus/w1/devices/` (taking for granted that everything have gone smooth on step 2 in this tutorial).
