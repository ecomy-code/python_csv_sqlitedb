import sqlite3
import csv
import os
miruta = os.path.abspath(os.getcwd())


conexion = sqlite3.connect(r"\ejemplo.db")
cursor = conexion.cursor()

def datos_del_csv():
  archivo = open("datos_db.txt" , 'w') #archivo vacio
  filas = csv.reader(archivo)
  return filas

def verificar_base_de_datos_sqlite():
  query1 = "create table if not exists estudiantes(nombre varchar (255), apellido  varchar (255),len  varchar (255),som  varchar (255))"
  query2 = "SELECT * FROM estudiantes"
  querys =[query1 , query2]
  for i in querys:
    cursor.execute(i)
    conexion.commit()
  

try:
  filas = datos_del_csv()
  cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", filas)
  print(cursor.fetchall())
  conexion.commit()
except Exception as e:
  print ('Error al agregar datos: ' + str(e))
conexion.close()
