#include <ESP8266WiFi.h>
#include <PubSubClient.h> //biblioteca MQTT
const char* ssid = ""; //SSID
const char* password = ""; //PASSWORD de la red
const char* mqtt_server = "xxxxx.ddns.net"; //Broker
int lectura;
int lux;
WiFiClient espClient;
PubSubClient client(espClient);
char mensaje[100]; //Tamaño del mensaje que vamos a mandar
int i = 0; //contador
void setup_wifi() { //función para conectarse al wifi
WiFi.mode(WIFI_STA);
WiFi.begin(ssid, password);
}
void reconnect() { //función que conecta o reconecta
while (!client.connected()) {
String clientId = "ESP8266Client-";//genera un nombre para el dispositivo
clientId += String(random(0xffff), HEX);
if (client.connect(clientId.c_str())) {
//client.publish("topico_de_prueba", "Conexión establecida"); //conecta
client.subscribe("topico_de_prueba"); //conecta y suscribe
} else {
delay(5000); //espera para reconectar o conectar
}
}
}
void setup() {
setup_wifi();
client.setServer(mqtt_server, 1883); //inicia servidor, puerto 80
Serial.begin(9600);
}
void loop() {
// lectura=analogRead(A0);
// Serial.println(lectura);
if (!client.connected()) { //si no se ha conectado, reconecta
reconnect();
}
client.loop();
lectura=analogRead(A0);
lux = -0.19 * (lectura - 1024) + 45;
Serial.println(lux);
Serial.println(lectura);
snprintf(mensaje, 100, "%d", lux);
client.publish("topico_de_prueba", mensaje); //publicar mensaje
delay(500); //espera 500ms
}