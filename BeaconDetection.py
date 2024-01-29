# BLE SCAN PROGRAM
import requests
import random
import time
import threading
# for scanning for BLE devices
from gattlib import DiscoveryService

PATIENT_MAC_ADDRESSES = ["D7:DA:5D:26:87:08", "E2:CB:C3:5C:C1:9A", "D8:F1:CA:B2:7A:04"]

# MAC address to patient mapping
mac_address_to_patient = {
    "D7:DA:5D:26:87:08": "Marco",
    "E2:CB:C3:5C:C1:9A": "Luca",
    "D8:F1:CA:B2:7A:04": "Francesco"
    # Add more mappings as needed
}

SERVER_URL = "http://192.168.1.5:3000"

message = "hello"

data = {"message": message}

try:
    response= requests.post(SERVER_URL+"/api/receiveMessage", json=data)

    if response.status_code == 200:
        print("Message sent succesfully.")
    else:
        print("Status code: {response.status_code}")

except requests.RequestException as e:
    print("Error : {e}")

# SCAN function
def scan( str, str1 ):
    print("Scanning for {}...\n".format(str1))
    service = DiscoveryService()
    devices = service.discover(8)

    for address, name in devices.items():
        if address == str:
            print("Address : {}\n".format(address))
            print("Beacon found - Patient: {}\n".format(str1))
            return True

    return False


# setting each device to false at first, if it is found in scan, will be turned to true
AllDev = True
dev1 = False
dev2 = False
dev3 = False


# setting a counter for each device
count1 = 0
count2 = 0
count3 = 0
count4 = 0

# setting each device to their address Ex: "0C:F3:EE:0D:79:5B"
beacon1 = "D7:DA:5D:26:87:08"
beacon2 = "E2:CB:C3:5C:C1:9A"
beacon3 = "D8:F1:CA:B2:7A:04"
beacon4 = "XX:XX:XX:XX:XX:XX"

# naming each device,
patient1 = "Marco"
patient2 = "Luca"
patient3 = "Francesco"

# ANOMALIES SIMULATION

def simulate_anomalies():

    # Simulate random anomalies for a random patient
    mac_address = random.choice(list(mac_address_to_patient.keys()))
    patient_name = mac_address_to_patient.get(mac_address, "Unknown")
    anomaly_type = random.choice(["temperature", "bpm_high","bpm_low", "fall_detection"])

    if anomaly_type == "temperature":
        value = random.uniform(38.0, 40.0)  # Simulate body temperature between 38.0 and 40.0 degrees Celsius
    elif anomaly_type == "bpm_high":
        value = random.randint(100, 160)  # Simulate BPM between 100 and 160
    elif anomaly_type == "bpm_low":
        value = random.randint(30, 60)  # Simulate BPM between 30 and 60
    else:  # fall_detection
        value = True  # Simulate fall detection as True

    payload = {"mac_address": mac_address, "patient": patient_name, "anomaly_type": anomaly_type, "value": value}

    # Send anomaly data to the server
    try:
        response = requests.post(f"{SERVER_URL}/api/update_anomaly", json=payload)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Anomaly sent successfully: {payload}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending anomaly: {e}")

    time.sleep(random.randint(5, 10))  # Simulate anomalies occurring every 10 to 15 seconds

def anomaly():
    while True:
        simulate_anomalies()

def run_anomaly_sim():
    anomaly_thread = threading.Thread(target=anomaly)
    anomaly_thread.start()

run_anomaly_sim()

# main file
while AllDev == True:

    # patient 1 block

    dev1 = scan(beacon1, patient1)
    if dev1 == True:
        print("Found\n")
        # Send POST request to the server
        try:
            # Send data to the server
            payload = {"mac_address": beacon1, "location": "room1", "patient": patient1, "status": "found"}
            response = requests.post(SERVER_URL+"/api/update_location", json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Location sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error sending message: {e}")
        count1 = 0
    if dev1 == False:
        print("Not Found\n")
        # Send POST request to the server
        try:
            # Send data to the server
            payload = {"mac_address": beacon1, "location": "room1", "patient": patient1, "status": "not found"}
            response = requests.post(SERVER_URL + "/api/update_location", json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Location sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error sending message: {e}")
        count1 += 1
    if count1 == 3:
        print("Sending Alert\n")



    # patient 2 block

    dev2 = scan(beacon2, patient2)
    if dev2 == True:
        print("Found\n")
        # Send POST request to the server
        try:
            # Send data to the server
            payload = {"mac_address": beacon2, "location": "room1", "patient": patient2, "status": "found"}
            response = requests.post(SERVER_URL+"/api/update_location", json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Location sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error sending message: {e}")
        count2 = 0
    if dev2 == False:
        print("Not Found\n")
        # Send POST request to the server
        try:
            # Send data to the server
            payload = {"mac_address": beacon2, "location": "room1", "patient": patient2, "status": "not found"}
            response = requests.post(SERVER_URL + "/api/update_location", json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Location sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error sending message: {e}")
        count2 += 1
    if count2 == 3:
        print("Sending Alert\n")

    # patient 3 block

    dev3 = scan(beacon3, patient3)
    if dev3 == True:
        print("Found\n")
        # Send POST request to the server
        try:
            # Send data to the server
            payload = {"mac_address": beacon3, "location": "room1", "patient": patient3, "status": "found"}
            response = requests.post(SERVER_URL+"/api/update_location", json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Location sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error sending message: {e}")
        count3 = 0
    if dev3 == False:
       print("Not Found\n")
       # Send POST request to the server
       try:
           # Send data to the server
           payload = {"mac_address": beacon3, "location": "room1", "patient": patient3, "status": "not found"}
           response = requests.post(SERVER_URL + "/api/update_location", json=payload)

           # Check if the request was successful (status code 200)
           if response.status_code == 200:
               print("Location sent successfully.")
           else:
               print(f"Failed to send message. Status code: {response.status_code}")

       except requests.RequestException as e:
           print(f"Error sending message: {e}")

       count3 += 1

    if count3 == 3:
        print("Sending Alert\n")


