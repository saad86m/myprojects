import json
import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=iot-hub-environment.azure-devices.net;DeviceId=sensor_001;SharedAccessKey=DzlnuKPcfH3VG9keLzEMtFE8iNWwXOFXw+saKTZmrGY="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_sensor_data():
    while True:
        data = {
            "device_id": "sensor_001",
            "temperature": random.uniform(20.0, 35.0),
            "humidity": random.uniform(30.0, 70.0),
            "air_quality": random.uniform(50, 150),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        message = Message(json.dumps(data))
        client.send_message(message)
        print(f"Data sent: {data}")
        time.sleep(5)

send_sensor_data()
