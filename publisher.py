import time
import paho.mqtt.client as mqtt

BROKER = "broker"
PORT = 1883
TOPIC = "vehicle/telemetry"

print("[Publisher] Connecting to broker...", flush=True)
client.username_pw_set("my_device_user", "your_chosen_password")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "PythonPublisher")
client.connect(BROKER, PORT, 60)

count = 1
while True:
    message = f"Engine RPM: {2000 + (count * 10)} | Speed: {60 + count}mph"
    client.publish(TOPIC, message)
    print(f"[Publisher] Sent -> {message}", flush=True)
    
    count += 1
    time.sleep(3)
