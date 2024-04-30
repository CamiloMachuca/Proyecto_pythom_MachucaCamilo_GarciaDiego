#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarCampers():
    listaCamper=[]
    with open('Campers.json','r') as openfile:
        listaCamper= json.load(openfile)

    return listaCamper

def menu_estudiante ():
    booleano=True
    while booleano==True:
        print("(1)informacion del estudiante")
        print("(2)volver al menu prinpal")
        

    opcion=input("ingrese la opcion deseada campers: ")
    if opcion=="1":
        mostrarCampers()
        id=input("ingrese el id del estudiante a campers")


def guardarArchivo(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Campers.json","w") as outfile:
        json.dump(miData,outfile)


def matriculaCampers():
    listaCamper=mostrarCampers()
    grupo=input("Ingrese el grupo en el cual se va a matricular el camper los grupos disponibles son T1, T2, T3: ")
    for grupo in listaCamper:
        id= input("ingrese el id que va a tener el camper")




