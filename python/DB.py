import mariadb
import sys
import time
from datetime import datetime

try:
    conexion = mariadb.connect(user="root", password="", database="cultivo")
    
except mariadb.Error as e:
    print("ERROR")
    sys.exit(1)

cur = conexion.cursor()

#cur.execute("SELECT matricula FROM Alumno")

#for matricula in cur:
#    print({matricula})

while True:
    arch = open("/var/www/html/electro1.txt", "r")
    electrovalvula_1 = arch.readline()
    arch.close()
    
    arch = open("/var/www/html/electro2.txt", "r")
    electrovalvula_2 = arch.readline()
    electrovalvula_2 = electrovalvula_2[2:11]
    arch.close()
    
    arch = open("/var/www/html/temp.txt", "r")
    temp = arch.readline()
    temp = temp[2:4]
    arch.close()
    
    arch = open("/var/www/html/lux.txt", "r")
    luz = arch.readline()
    arch.close()
    
    arch = open("/var/www/html/agua.txt", "r")
    nivel = arch.readline()
    arch.close()
    
    arch = open("/var/www/html/humedad1.txt", "r")
    hum1 = arch.readline()
    arch.close()
    
    arch = open("/var/www/html/humedad2.txt", "r")
    hum2 = arch.readline()
    hum2 = hum2[2:14]
    arch.close()
    
    arch = open("/var/www/html/humedad3.txt", "r")
    hum3 = arch.readline()
    hum3 = hum2[0:15]
    arch.close()

    
    fecha = datetime.now()

    try: 
        cur.execute("INSERT INTO Sensores ( `Electrovalvula 1`,`Electrovalvula 2`,`Temperatura`,`Luminosidad`,`Nivel de agua`,`Sensor humedad 1`,`Sensor humedad 2`,`Sensor humedad 3`,`Hora`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(electrovalvula_1,electrovalvula_2,temp,luz,nivel,hum1,hum2,hum3,fecha))

    except mariadb.Error as e:
        print(f"Error: {e}")
    conexion.commit()
    time.sleep(1800)
    print("Línea agregada a DB")
