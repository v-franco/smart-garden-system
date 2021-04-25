import paho.mqtt.publish as publicar
import RPi.GPIO as GPIO
import timeGPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
variable = False
while True:
    variable=GPIO.input(8)
    if variable == False:
        publicar.single('topico_de_prueba', ' insuficiente', hostname='namacuix272.ddns.net')
    else:
        publicar.single('topico_de_prueba', ' correcta ', hostname='namacuix272.ddns.net')
        time.sleep(0.5)