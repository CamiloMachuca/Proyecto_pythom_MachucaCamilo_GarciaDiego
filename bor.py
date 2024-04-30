
"""
c=input("ingresa la cantidad de notas: ")
contador=0
nota=[]
for i in c:
    n=input("ingresa nota: ")
    contador=+1
    nota=n

    Nota_Final= (nota(i)*c)
    print(Nota_Final)
""" 
#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarCampers():
    listaCamper=[]
    with open('Campers.json','r') as openfile:
        listaCamper= json.load(openfile)
        
    return listaCamper
# funcion para guardar los cambios de un Json
def guardarArchivo(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Campers.json","w") as outfile:
        json.dump(miData,outfile)

lista=[]
lista = mostrarCampers()# se llaman a los datos que hay en el Json para asi previamente mostrarlos
print(lista)
"""
for i in lista:
    print("ID:",i["id"])
    print("nombres:",i["nombres"])
    print("Apellidos:",i["apellidos"])
    print("direccion:",i["direccion"])
    print("acudiente:",i["acudiente"])
    print("telefono celular:",i["celular"])
    print("telefono fijo:",i["fijo"])
    print("estado:",i ["estado"])
    print("riesgo:",i ["riesgo"])
"""

#Funcion para agregar si un estudiante esta aprobado o reprobado  rutas 
campers = int(input("Cual numero de identificacion vas a cambiar?"))
estado=input("cual es el estado del camper ")


lista[0]["estudiantes"][campers-1]["estado"] = estado
guardarArchivo(lista)
print("Cambio realizado!")




# programa para agregar las notas y sacar el total de las notas
nota1=input("Ingrese la nota de la  prueba teórica: ")
nota2=input("Ingrese la nota de la prueba practica: ")
nota3=input("Ingrese la nota de del primer taller")
nota4=input("ingrese la nota del segundo taller ")
notaFinal=(nota1*0.3)+(nota2*0.6)+(nota3*0.05)+(nota4*0.05)


#programa para asignar los campers a una ruta