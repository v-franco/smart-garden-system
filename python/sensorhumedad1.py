import RPi.GPIO as GPIO
import time
#Hacemos el pin 12 entrada
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
variable = False
while True:
  #print("El led tiene una condicion logica:  ", variable)
  variable=GPIO.input(8)
  if variable == True:
      msg = "insuficiente"
      archivo= open("/var/www/html/humedadvic.html", "w+")
      archivo.write("<html><head><title>Sensor de humedad</title><meta http-equiv='refresh' content='0.5'/></head><body><p>La humedad actual en planta 1 es: </p>"+msg+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
      archivo.close()
      archivo2 = open("/var/www/html/humedad1.txt", "w+")
      archivo2.write(str(msg))
      archivo2.close()
  else:
      msg="correcta"
      archivo= open("/var/www/html/humedadvic.html", "w+")
      archivo.write("<html><head><title>Sensor de humedad</title><meta http-equiv='refresh' content='0.5'/></head><body><p>La humedad actual en planta 1 es: </p>"+msg+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
      archivo.close()
      archivo2 = open("/var/www/html/humedad1.txt", "w+")
      archivo2.write(str(msg))
      archivo2.close()
  time.sleep(0.1)

        

