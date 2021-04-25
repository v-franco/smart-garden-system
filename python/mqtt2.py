import paho.mqtt.subscribe as suscribir
while True:
    mensaje = suscribir.simple("topico_de_prueba", hostname="192.168.1.79")
    print(mensaje.topic)
    print(mensaje.payload)
    msg = mensaje.payload
    msgtxt = mensaje.payload
    
    if str(msgtxt) == "b'insuficiente'" or str(msg) == "b'correcta    '":
        archivo= open("/var/www/html/humedadhorace.html", "w+")
        archivo.write("<html><head><title>Sensor humedad 2</title><meta http-equiv='refresh' content='0.5'/></head><body><p>El nivel de humedad de la planta 2 es: </p>"+str(msgtxt)+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
        archivo.close()
        archivo2 = open("/var/www/html/humedad2.txt", "w+")
        archivo2.write(str(msg))
        archivo2.close()
        
    elif str(msgtxt) == "b' insuficiente'" or str(msg) == "b' correcta    '":
        archivo= open("/var/www/html/humedadjp.html", "w+")
        archivo.write("<html><head><title>Sensor humedad 3</title><meta http-equiv='refresh' content='0.5'/></head><body><p>El nivel de humedad de la planta 3 es: </p>"+str(msgtxt)+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
        archivo.close()
        archivo2 = open("/var/www/html/humedad3.txt", "w+")
        archivo2.write(str(msg))
        archivo2.close()
        
    elif str(msgtxt) == "b'Encendida'" or str(msg) == "b'Apagada  '":
        archivo2 = open("/var/www/html/electro2.txt", "w+")
        archivo2.write(str(msg))
        archivo2.close()
    else:
        
            if  int(msg) < 40:
                archivo= open("/var/www/html/temperatura.html", "w+")
                archivo.write("<html><head><title>Sensor de temperatura</title><meta http-equiv='refresh' content='0.5'/></head><body><p>La temperatura actual (Celsius) es: </p>"+str(msg)+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
                archivo.close()
                archivo2 = open("/var/www/html/temp.txt", "w+")
                archivo2.write(str(msg))
                archivo2.close()
            
        
            if int(msg) > 40 and int(msg) < 980:
                msg1 = int(msg)-45
                archivo= open("/var/www/html/lux.html", "w+")
                archivo.write("<html><head><title>Sensor de luz</title><meta http-equiv='refresh' content='0.5'/></head><body><p>El nivel de iluminacion (lux) es: </p>"+str(msg1)+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
                archivo.close()
                archivo2 = open("/var/www/html/lux.txt", "w+")
                archivo2.write(str(msg1))
                archivo2.close()
            

            if int(msg) > 999:
                msg2 = ""
                if int(msg) <= 1510:
                    msg2 = "nivel bajo"
                if int(msg) > 1511 and int(msg) < 1600:
                    msg2 = "nivel normal"
                if int(msg) > 1600:
                    msg2 = "nivel optimo"
                archivo= open("/var/www/html/tanque.html", "w+")
                archivo.write("<html><head><title>Sensor de agua</title><meta http-equiv='refresh' content='0.5'/></head><body><p>El nivel de tanque es: </p>"+str(msg2)+'<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a></body></html>')
                archivo.close()
                archivo2 = open("/var/www/html/agua.txt", "w+")
                archivo2.write(str(msg2))
                archivo2.close()
