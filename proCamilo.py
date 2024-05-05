#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarTrainers():
    listaTrainer=[]
    with open('trainers.json','r') as openfile:
        listaTrainer= json.load(openfile)

    return listaTrainer
def guardarArchivoTrainers(miDato):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("trainers.json","w") as outfile:
        json.dump(miDato,outfile)


#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarCampers():
    listaCampers=[]
    with open('Campers.json','r') as openfile:
        listaCampers= json.load(openfile)

    return listaCampers
def guardarArchivoCampers(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Campers.json","w") as outfile:
        json.dump(miData,outfile)







import json
# funcion para mostrar los datos del Json
def mostrarRutas():
    listaRutas=[]
    with open('rutas.json','r') as openfile:
        listaRutas= json.load(openfile)

    return listaRutas
def guardarArchivoRutas(miDato1):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("rutas.json","w") as outfile:
        json.dump(miDato1,outfile)

"""
print("##########################################")
print("============= Menu coordinador ===========")
print("##########################################")
print("(1)agregar nota del examen de ingreso\n(2)Añadir nuevo campers\n(3)asignar notas a los campers\n(4)Asignar las rutas de entrenamiento a los grupos\n(5)Crear nuevas rutas\n(6)asignar los trainers encargados de cada ruta\n(7)realizar reportes")
opc=input("Ingrese la opcion deseada: ")
if opc=="4":
    print("asignar la ruta de entrenamiento a los grupos")"""



#Opciones para los reportess
#opcion 2 de reportes
print("(2)Listar los **campers** que aprobaron el examen inicial.")
datosCampers= mostrarCampers()
campersAprobados=[]# se crea una lista para separar a los campers que pasaron la inscipcion

for grupo in datosCampers:
        
        for campe in grupo["campers"]:
            if campe["estado"]=="Aprobado":
                campersAprobados.append(campe)
cantidadCampers= len(campersAprobados)
for i in campersAprobados:
    print("ID:",i["id"])
    print("Nombre:",i["nombres"])
    print("Apellido:",i["apellidos"])
    print("direccion:",i["direccion"])
    print("acudiente",i["acudiente"])
    print("estado",i["estado"])
print("La cantidad de campers inscritos son: ",cantidadCampers)






#opcion 4 de reportes
print("(4)Listar los **campers** que cuentan con bajo rendimiento.")
datosCampers= mostrarCampers()
campersRendimientoBajo=[]# se crea una lista para separar a los campers con bajo rendimiento

for grupo in datosCampers:
        
        for campe in grupo["campers"]:
            if campe["riesgo"]=="bajo":
                campersRendimientoBajo.append(campe)
cantidadCampers= len(campersRendimientoBajo)
for i in campersRendimientoBajo:
    print("ID:",i["id"])
    print("Nombre:",i["nombres"])
    print("Apellido:",i["apellidos"])
    print("direccion:",i["direccion"])
    print("acudiente",i["acudiente"])
    print("estado",i["estado"])
print("La cantidad de campers inscritos son: ",cantidadCampers)










#Punto 5 de reportes
print("(5)Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.")
datosCampers= mostrarCampers()
campersAsignadoRuta=[]# se crea una lista para separar a los campers que pasaron la inscipcion

for grupo in datosCampers:
        
        for campe in grupo["campers"]:
            if campe["ruta"]!="no asignado":
                campersAsignadoRuta.append(campe)
cantidadCampers= len(campersAsignadoRuta)
for i in campersAsignadoRuta:
    print("ID:",i["id"])
    print("Nombre:",i["nombres"])
    print("Apellido:",i["apellidos"])
    print("direccion:",i["direccion"])
    print("acudiente",i["acudiente"])
    print("estado",i["estado"])
print("La cantidad de campers inscritos son: ",cantidadCampers)
print()
datosTrainers= mostrarTrainers()
TrainersRuta=[]

for dato in datosTrainers:
        
        for campe in dato["trainer"]:
            if campe["ruta"]!="no asignado":
                TrainersRuta.append(campe)
cantidadCampers= len(TrainersRuta)
for i in TrainersRuta:
    print("ID:",i["id"])
    print("Nombre:",i["nombres"])
    print("Apellido:",i["apellidos"])
    print("direccion:",i["direccion"])
    print("acudiente",i["acudiente"])
    print("estado",i["estado"])
print("La cantidad de campers inscritos son: ",cantidadCampers)












