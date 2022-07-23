import paho.mqtt.client as mqtt

client = mqtt.Client(
    client_id="2g2g2h4",
    clean_session=True
)
client.username_pw_set("arief", "arief")


client.connect('broker.emqx.io', 1883)

while True:
    client.publish('arief/test', input('Message: '))