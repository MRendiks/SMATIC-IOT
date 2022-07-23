import paho.mqtt.client as mqtt
import os

from .subscribe import on_message, on_connect

client = mqtt.Client(
    client_id=os.getenv("MQTT_CLIENT_ID"),
    clean_session=True
)

client.username_pw_set(os.getenv("MQTT_USERNAME"), os.getenv("MQTT_PASSWORD"))

client.connect(os.getenv("MQTT_BROKER"), int(os.getenv("MQTT_PORT")))


client.on_connect = on_connect
client.on_message = on_message
