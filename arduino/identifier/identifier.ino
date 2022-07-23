#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <PubSubClient.h>

const char *ssid = "kebaratan"; 
const char *password = "Wifinyalemot";

#define VENDOR "ESP8266" // change to your vendor type
#define DEVICE_NAME "Identifier"

#define MQTT_BROKER "broker.hivemq.com"
#define REGISTER_TOPIC "enMH7b6VPcfylubsL/register"
String FIND_TOPIC = "enMH7b6VPcfylubsL/find";
#define MQTT_USERNAME "smatic-staging"
#define MQTT_PASSWORD "SemarIoT2022"
#define MQTT_PORT 1883

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  D2  // ESP32 pin GIOP5 
#define RST_PIN D1 // ESP32 pin GIOP27 
#define pin_LED D8

MFRC522 rfid(SS_PIN, RST_PIN);

WiFiClient espClient;
PubSubClient client(espClient);

String macAddress = "";
String subTopic = "";

void setup() {
  pinMode(pin_LED, OUTPUT);
  digitalWrite(pin_LED, LOW);
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

  // rfid
  SPI.begin(); // init SPI bus
  rfid.PCD_Init(); // init MFRC522 
  
  //connecting to a mqtt broker
  client.setServer(MQTT_BROKER, MQTT_PORT);
  client.setCallback(callback);
  while (!client.connected()) {
      String client_id = String(WiFi.macAddress());
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
  String payload = String(WiFi.macAddress()) + "," + VENDOR + "," + DEVICE_NAME;
  // publish and subscribe
  client.publish(REGISTER_TOPIC, payload.c_str());
  subTopic = FIND_TOPIC + "/" + macAddress;
  client.subscribe(subTopic.c_str());
  Serial.print("Find Topic: ");
  Serial.println(subTopic);
  Serial.println("-----------------------");
}

void loop() {
  // put your main code here, to run repeatedly:
  client.loop();

  digitalWrite(pin_LED, LOW);

  if (rfid.PICC_IsNewCardPresent()) { // new tag is available
    if (rfid.PICC_ReadCardSerial()) { // NUID has been readed
      String rfidTag = readRFID();
      
      Serial.print("Tag: ");
      Serial.println(rfidTag);
      Serial.println("-----------------------");
      
      client.publish(FIND_TOPIC.c_str(), rfidTag.c_str());
    }
  }

}

void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  String message = "";
  for (int i = 0; i < length; i++) {
      message += (char) payload[i];
  }
  Serial.print(message);
  Serial.println();
  Serial.println("-----------------------");

  if(message == "1"){
    digitalWrite(pin_LED, HIGH);
    delay(1000);
  }
}

String readRFID(){
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
//  Serial.print("RFID/NFC Tag Type: ");
//  Serial.println(rfid.PICC_GetTypeName(piccType));

  String tag = "";
  for (int i = 0; i < rfid.uid.size; i++) {
    tag += rfid.uid.uidByte[i] < 0x10 ? "0" : ":";
    tag += String(rfid.uid.uidByte[i], HEX);
  }

  rfid.PICC_HaltA(); // halt PICC
  rfid.PCD_StopCrypto1(); // stop encryption on PCD

  return tag;
}
