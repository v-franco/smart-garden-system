#!/usr/bin/python

import cgi, cgitb, socket, sys

class LibroController:
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
        print('<br><a href="/electrovalvulavic.html"><button type="button">Regresar a control</button></a>')
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
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Enciende'
                sock.send(mensaje)
                sock.close()
        elif datos=="2":
                estado = "Apagada"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Apaga'
                sock.send(mensaje)
                sock.close()
        elif datos=="3":
                estado = "Apagada y server desconectado"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Salir'
                sock.send(mensaje)
                sock.close()
        elif datos=="4":
                estado = "Auto on"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Auto on'
                sock.send(mensaje)
                sock.close()
        elif datos=="5":
                estado = "Auto off"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Auto off'
                sock.send(mensaje)
                sock.close()
        elif datos=="6":
                estado = "Enciende siempre"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_adress = ('192.168.1.79', 8080)
                sock.connect(server_adress)
                mensaje=b'Enciende siempre'
                sock.send(mensaje)
                sock.close()
        this.respuestaServer(datos, estado)
        

#Crear el objeto cgi
libro = LibroController()
libro.procesarTransaccion()
