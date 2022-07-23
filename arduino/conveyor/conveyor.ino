#include <WiFi.h>

const char *ssid = "kebaratan"; 
const char *password = "Wifinyalemot";

#define VENDOR "ESP32" // change to your vendor type
#define DEVICE_NAME "Conveyor"

#define MQTT_BROKER "broker.hivemq.com"
#define REGISTER_TOPIC "enMH7b6VPcfylubsL/register"
#define MQTT_USERNAME "smatic-staging"
#define MQTT_PASSWORD "SemarIoT2022"
#define MQTT_PORT 1883

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5  // ESP32 pin GIOP5 
#define RST_PIN 27 // ESP32 pin GIOP27 

MFRC522 rfid(SS_PIN, RST_PIN);

const int pinSensorA[2] = {5, 18}; // {Trig, Echo}
#define SOUND_VELOCITY 0.034


void setup() {
  Serial.begin(9600);
//  pinMode(pinSensorA[0], OUTPUT);
//  pinMode(pinSensorA[1], INPUT);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Max address: ");
  Serial.println(WiFi.macAddress());
  Serial.println("Connected to the WiFi network");
  Serial.println("-----------------------");

  // rfid
  SPI.begin(); // init SPI bus
  rfid.PCD_Init(); // init MFRC522

}

void loop() {
  // put your main code here, to run repeatedly:
  if (rfid.PICC_IsNewCardPresent()) { // new tag is available
    if (rfid.PICC_ReadCardSerial()) { // NUID has been readed
      String rfidTag = readRFID();
      
      Serial.print("Tag: ");
      Serial.println(rfidTag);
      Serial.println("-----------------------");
     
    }
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

//float sensorAValue(){
//  // Clears the trigPin
//  digitalWrite(pinSensorA[0], LOW);
//  delayMicroseconds(2);
//  // Sets the trigPin on HIGH state for 10 micro seconds
//  digitalWrite(pinSensorA[0], HIGH);
//  delayMicroseconds(10);
//  digitalWrite(pinSensorA[0], LOW);
//
//  long duration = pulseIn(pinSensorA[1], HIGH);
//
//  float distanceCm = duration * SOUND_VELOCITY/2;
//
//  return distanceCm;
//}
