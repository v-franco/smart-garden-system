# smart-garden-system
IoT based smart gardening system

# Overview
This project consists of a IoT smart gardenign system using a Raspberry Pi and 3 NodeMCUs located in different households. 

# Physical installation
This project required the use of electronic materials such as breadboards, solenoid valves (127V, 60Hz), relay modules, thermistors (10k ohms), humidity sensors, UTP cable, jumper cables, etc.
Full materials list link here: 

# Technologies used
This project employs the use of a DDNS Web Server redirected to the Raspberry Pi, which has installed Apache2, MariaDB, and PHP.

The connection is made using Sockets and MQTT.

The database used was MariaDB, and the connection to the DB was made through Python.
The DB querys were made using PHP. 

The NodeMCUs were programmed with Arduino IDE to read and send through MQTT data recolected from sensors monitoring temperature, humidity, light, and water levels.

# Authors
This videogame was made by [@BeanIRL](https://github.com/BeanIRL), [@A01367213](https://github.com/A01367213), and @v-franco