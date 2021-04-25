#!/usr/bin/python

import cgi, cgitb, socket, sys

class LibroController:

   # biblio=bibliotecaAD()

    def __init__(this):
        this.op=""
        this.boton=""

    def respuestaServer(this, datos, estado):
        print("Content-type: text/html\n\n")
        print("<html>")
        print("<head><title></title></head>")
        print("<body>")
        print("<h2> ESTADO ELECTROVALVULA </h2>")
        print("<h2> ELECTROVALVULA: "+estado+"</h2>")
        print('<br><a href="/electrovalvulajp.html"><button type="button">Regresar a control</button></a>')
        print('<br><a href="/menuPrincipal.html"><button type="button">Regresar a menu</button></a>')
        print("</body>")
        print("</html>")

    def obtenerDatos(this):
        cgitb.enable()
        formLibro = cgi.FieldStorage()
        
        this.op=formLibro.getvalue("opcion")
        this.boton=formLibro.getvalue("boton")
        
        datos=str(this.op)

        return datos

    def procesarTransaccion(this):
        datos = this.obtenerDatos()

        if datos=="1":
                estado = "Encendida"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('hahayou.ddns.net', 8080)
                sock.connect(server_adress)
                mensaje=b'Enciende'
                #print('Enviando (!r)'.format(mensaje))
                sock.send(mensaje)
                sock.close()
        elif datos=="2":
                estado = "Apagada"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('hahayou.ddns.net', 8080)
                sock.connect(server_adress)
                mensaje=b'Apaga'
                #print('Enviando (!r)'.format(mensaje))
                sock.send(mensaje)
                sock.close()
        elif datos=="3":
                estado = "Apagada y server desconectado"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('hahayou.ddns.net', 8080)
                sock.connect(server_adress)
                mensaje=b'Salir'
                #print('Enviando (!r)'.format(mensaje))
                sock.send(mensaje)
                sock.close()
            #print("Opcion no encontrada")
        this.respuestaServer(datos, estado)
        

#Crear el objeto cgi
libro = LibroController()
libro.procesarTransaccion()

