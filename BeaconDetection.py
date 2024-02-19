# BLE SCAN PROGRAM
import requests
import random
import time
import threading
# for scanning for BLE devices
from gattlib import DiscoveryService

SERVER_URL = "http://192.168.1.5:3000"

Room = "Room 1"

# Function to fetch MAC address to patient mapping from the server
def fetch_mac_address_mapping():
    try:
        # Replace 'your_server_url' with the actual URL of your server
        response = requests.get(f"{SERVER_URL}/api/get_mac_address_mapping")

        if response.status_code == 200:
            # Assuming the server responds with JSON data
            return response.json()
        else:
            print(f"Error fetching MAC address mapping: {response.status_code}")
            return {}
    except Exception as e:
        print(f"Error fetching MAC address mapping: {str(e)}")
        return {}

# Fetch MAC address to patient mapping
mac_address_to_patient = fetch_mac_address_mapping()

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

    time.sleep(random.randint(25, 60))  # Simulate anomalies occurring every 25 to 60 seconds

def anomaly():
    while True:
        simulate_anomalies()

def run_anomaly_sim():
    anomaly_thread = threading.Thread(target=anomaly)
    anomaly_thread.start()

run_anomaly_sim()

def fetch():
    while True:
        fetch_mac_address_mapping()
        time.sleep(60)

def fetch_mac_address():
    fetch_thread = threading.Thread(target=fetch)
    fetch_thread.start()
   
fetch_mac_address()

def scan_and_send(beacon, patient):
    dev = scan(beacon, patient)
            if dev == True:
                print("Found\n")
                # Send POST request to the server
                try:
                    # Send data to the server
                    payload = {"mac_address": beacon, "location": Room, "patient": patient, "status": "found"}
                    response = requests.post(SERVER_URL+"/api/update_location", json=payload)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        print("Location sent successfully.")
                    else:
                        print(f"Failed to send message. Status code: {response.status_code}")

                except requests.RequestException as e:
                    print(f"Error sending message: {e}")

            if dev == False:
                print("Not Found\n")
                # Send POST request to the server
                try:
                    # Send data to the server
                    payload = {"mac_address": beacon, "location": Room, "patient": patient, "status": "not found"}
                    response = requests.post(SERVER_URL + "/api/update_location", json=payload)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        print("Location sent successfully.")
                    else:
                        print(f"Failed to send message. Status code: {response.status_code}")

                except requests.RequestException as e:
                    print(f"Error sending message: {e}")

# main file
while True:
    # Iterate over the MAC address to patient mapping
    for beacon_mac, patient_name in mac_address_to_patient.items():
        scan_and_send(beacon_mac, patient_name)
