import paho.mqtt.publish as publicar
import socket
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
auto = False
# crear el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# asignar un socket a un puerto
direccion_servidor = ('192.168.1.250', 8080) #Dirección de servidor
print('comenzando a recibir conexiones {} en el puerto {}'.format(*direccion_servidor))
sock.bind(direccion_servidor)
# escuchando conexiones
sock.listen(1)
while True:
    # Esperando conexión
    print('Esperando mensajes y conexiones')
    conexion, direccion_cliente = sock.accept()
    try:
        print('Aceptando conexión de', direccion_cliente)
        dato_recibido=conexion.recv(1024) #Bytes
        print(dato_recibido)
        if dato_recibido==b'Enciende':
            msg = 'Encendida'
            print(msg)
            GPIO.output(10, False)
        elif dato_recibido==b'Apaga':
            msg='Apagada'
            print(msg)
            GPIO.output(10, True)
        elif dato_recibido==b'Salir':
            msg='Apagada'
            print(msg)
            GPIO.output(10, True)
            conexion.close()
            sock.close()break
        elif dato_recibido==b'Auto on':
            msg='Auto on'
            print(msg)
            auto = True
            while auto:
            sock.setblocking(False)
        try:
            print('Esperando mensajes y conexiones')
            conexion, direccion_cliente = sock.accept()
            print('Aceptando conexión de', direccion_cliente)
            dato_recibido=conexion.recv(1024) #Bytes
            print(dato_recibido)
            if dato_recibido==b'Auto off':
                GPIO.output(10, True)
                auto=False
                msg='Auto off'
                print(msg)
                sock.setblocking(True)
        except:
            print("continua programa")
            arch = open("/home/pi/Documents/humedad1.txt", "r")
            automatico = arch.readline()
            arch.close()
        if automatico == "correcta":
            GPIO.output(10, True)
            publicar.single('topico_de_prueba', 'Apagada ',
            hostname='namacuix272.ddns.net')
            msg1 = "Apagada"
            time.sleep(1)
        elif automatico == "insuficiente":
            GPIO.output(10, False)
            publicar.single('topico_de_prueba', 'Encendida',
            hostname='namacuix272.ddns.net')
            msg1 = "Encendida"
            time.sleep(1)
        else:
            print('Opcion no disponible')
    finally:
        conexion.close() #limpiar conexión