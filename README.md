**Neurodegenerative diseases monitoring: Alzheimer**

This is an Internet of Things (IoT) application designed to monitor and manage patient well-being through a combination of BLE beacon scanning and wearable device anomaly detection.
Wearable device anomaly detection is not the main focus of this educational project, that is the beacon detection.
The project leverages the Web of Things (WoT) paradigm to enhance device interoperability and create a real-time monitoring system.

In healthcare environments, timely and accurate information is crucial for ensuring patient safety. 
The project employs a Raspberry Pi as an edge device to scan for BLE beacons in the surroundings and communicate with a wearable device worn by the patient. 
The wearable device is equipped with sensors to monitor vital signs and detect anomalies such as falls. Seen that the main focus is the detection , anomalies and all the 
sensors data are simulated. 

![A9217561-6C1B-4200-8944-835E4B8182BE](https://github.com/UniSalento-IDALab-IoTCourse-2021-2022/wot-project-part1-MarcoStabile/assets/105797309/c321a90d-9993-454d-b2af-bb0f7425559c)

To set up and run the project, follow the step-by-step guide below.

(Node and npm are required)

First run the server with command:

node Server.js

On Raspberry Pi ensure that the following libraries are installed on the device and then run the following command:
<img width="218" alt="Screenshot 2024-01-29 alle 23 25 03" src="https://github.com/UniSalento-IDALab-IoTCourse-2021-2022/wot-project-part1-MarcoStabile/assets/105797309/35adb5a8-44d5-4e8e-b0a8-71a53d78cb0f">

*libbluetooth-dev
libboost-python-dev 
libboost-thread-dev 
libglib2.0-dev 
python-dev 
bluez 
pybluez 
gattlib*

The output should look like this:

****ADD IMAGE FROM RASPBERRY TERMINAL****

Then to monitor data and to recieve alert from the server you can open dashboard.html

***ADD DASHBOARD PHOTO***


