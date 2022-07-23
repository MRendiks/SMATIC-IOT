import paho.mqtt.client as mqtt
import os
from .subscribers.register_subscriber import register_subscriber


def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(os.getenv("MQTT_BASE_TOPIC") + "/register")


def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
    if message.topic == os.getenv("MQTT_BASE_TOPIC") + "/register":
        register_subscriber(message.payload.decode())

