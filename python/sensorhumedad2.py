import paho.mqtt.publish as publicar
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)
variable = False
while True:
    variable=GPIO.input(38)
    if variable == True:
        msg="insuficiente"
        publicar.single('topico_de_prueba', 'insuficiente', hostname='namacuix272.ddns.net')
        archivo2 = open("/home/pi/Documents/humedad1.txt", "w+")
        archivo2.write(str(msg))
        archivo2.close()
    else:
        msg="correcta"
        publicar.single('topico_de_prueba', 'correcta ', hostname='namacuix272.ddns.net')
        archivo2 = open("/home/pi/Documents/humedad1.txt", "w+")
        archivo2.write(str(msg))
        archivo2.close()
time.sleep(0.5)