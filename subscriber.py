import paho.mqtt.client as mqtt

BROKER = "broker"
PORT = 1883
TOPIC = "vehicle/telemetry"

def on_connect(client, userdata, flags, rc):
    print(f"[Subscriber] Connected with result code {rc}", flush=True)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"[Subscriber] Received on [{msg.topic}]: {msg.payload.decode()}", flush=True)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "PythonSubscriber")
client.username_pw_set("mundall", "Flipflop7#12")
client.on_connect = on_connect
client.on_message = on_message

print("[Subscriber] Connecting to broker...", flush=True)
client.connect(BROKER, PORT, 60)

# Blocking call that keeps listening for incoming messages
client.loop_forever()
