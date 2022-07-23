#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <PubSubClient.h>

const char *ssid = "kebaratan"; 
const char *password = "Wifinyalemot";

#define VENDOR "ESP8266" // change to your vendor type
#define DEVICE_NAME "Rack A"

#define MQTT_BROKER "broker.hivemq.com"
#define REGISTER_TOPIC "enMH7b6VPcfylubsL/register"
#define RACK_TOPIC "enMH7b6VPcfylubsL/rack"
#define MQTT_USERNAME "smatic-staging"
#define MQTT_PASSWORD "SemarIoT2022"
#define MQTT_PORT 1883

const int pinBottomSensor[2] = {D8, D7}; // {Trig, Echo}
const int pinTopSensor[2] = {D6, D5};
const int pinLed = D4;
//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034

WiFiClient espClient;
PubSubClient client(espClient);

String macAddress = "";

const int period = 1000;
unsigned long lastTime = 0;

void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(pinBottomSensor[0], OUTPUT); // Sets the trigPin as an Output
  pinMode(pinBottomSensor[1], INPUT); // Sets the echoPin as an Input
  pinMode(pinTopSensor[0], OUTPUT); // Sets the trigPin as an Output
  pinMode(pinTopSensor[1], INPUT); // Sets the echoPin as an Input
  
  pinMode(pinLed, OUTPUT);
  digitalWrite(pinLed, LOW);

  Serial.begin(115200);
  Serial.println();
  Serial.print("Configuring access point...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
   delay(500);
   Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Max address: ");
  Serial.println(WiFi.macAddress());
  Serial.println("Connected to the WiFi network");
  
  //connecting to a mqtt broker
  client.setServer(MQTT_BROKER, MQTT_PORT);
  client.setCallback(callback);
  while (!client.connected()) {
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
      if (client.connect(client_id.c_str(), MQTT_USERNAME, MQTT_PASSWORD)) {
          Serial.println("Public emqx mqtt broker connected");
      } else {
          Serial.print("failed with state ");
          Serial.print(client.state());
          delay(2000);
      }
  }

  macAddress = String(WiFi.macAddress());
  String payload = macAddress + "," + VENDOR + "," + DEVICE_NAME;
  // publish and subscribe
  client.publish(REGISTER_TOPIC, payload.c_str());
}

void loop() {
  unsigned long currentMilis = millis();
  
  client.loop();

  if(currentMilis - lastTime >= period){

    float topValue = topSensorValue();
    float bottomValue = bottomSensorValue();
    
    String message = String(topValue) + "," + String(bottomValue);
    String topic = String(String(RACK_TOPIC) + "/" + macAddress);

    client.publish(topic.c_str(), message.c_str());
  
    Serial.print(topValue);
    Serial.print(", ");
    Serial.println(bottomValue);
    
    lastTime = currentMilis;
  }
  
}

void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
      Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}

float bottomSensorValue(){
  // Clears the trigPin
  digitalWrite(pinBottomSensor[0], LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(pinBottomSensor[0], HIGH);
  delayMicroseconds(10);
  digitalWrite(pinBottomSensor[0], LOW);

  long duration = pulseIn(pinBottomSensor[1], HIGH);

  float distanceCm = duration * SOUND_VELOCITY/2;

  return distanceCm;
}

float topSensorValue(){
  // Clears the trigPin
  digitalWrite(pinTopSensor[0], LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(pinTopSensor[0], HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTopSensor[0], LOW);

  long duration = pulseIn(pinTopSensor[1], HIGH);

  float distanceCm = duration * SOUND_VELOCITY/2;

  return distanceCm;
}
