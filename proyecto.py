

# menu de opciones ya sea camper, Trainer o coordinador y cada uno va a tener un menu distinto de opciones disponibles


# diseñar un programa para saber que camper paso de estar inscrito a aprobado 

# Rutas disponibles: Ruta NodeJS, Ruta Java, Ruta NetCore capacidad maxima por ruta es de 33 campers

# Hay clases cada 4 horas serian un total de 3 clases diarias

# modulo de matricula Programa  para asignar la rutas de los campers esto lleva la Ruta, trainer encargado,fecha inicio y fecha final, salon de entrenamiento



# crear trainers que trabajen en campuslands

# Programa para saber la nota final de los campers ademas muestre los campers aprobados y los reprobados

# programa para sacar el rendimiento de los campers en cada modulo y que permita consultar esos datos




# funciones 
# funcion para que el coordinador pueda registrar la nota de los campers que se han registrado y con ello cambiar su estado a “Aprobado”. La prueba es aprobada si el promedio entre la nota teórica y la nota practica es mayor o igual a 60.



#funcion para mostrar la cantidad de campers que hay en estado de inscripcion
# funcion para saber los campers que pasaron el examen de ingreso
# funcion para que el coordinador pueda ver los datos de los trainers que trabajan en campusland
# funcion para sacar el rendimineto de los campers esto llevaria la nota final de cada camper en el modulo en el que se encuentra
# funcion para que el coordinador designe al trainer encargado de cada modulo 
#funcion para que el trainer ingrese las notas de los campers
#funcion para sacar la nota final de los campers en cada mudulo
# funcion para guardar los datos de los campers que perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado. debe de imprimirse el modulo en el que perdieron y con que trainers fue que perdieron


# funcion para que La **coordinación académica** pueda crear nuevas rutas y estas rutas se añadan al Json de rutas, las cuales contienen la siguiente información (módulos):
#- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
#- Programación Web (HTML, CSS y Bootstrap).
#- Programación formal (Java, JavaScript, C#).
#- Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
#- Backend (NetCore, Spring Boot, NodeJS y Express).
# ademas de crear nuevas rutas pueda designar los Trainers que van a estar a cargo de esas rutas
#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarTrainers():
    listaTrainer=[]
    with open('trainers.json','r') as openfile:
        listaTrainer= json.load(openfile)

    return listaTrainer


#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# funcion para mostrar los datos del Json
def mostrarCampers():
    listaCampers=[]
    with open('Campers.json','r') as openfile:
        listaCampers= json.load(openfile)

    return listaCampers
def guardarArchivo(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Campers.json","w") as outfile:
        json.dump(miData,outfile)



buclePrincipal=True
while buclePrincipal==True:
    print("========Menu de opciones=========")
    print("(1) campers")
    print("(2)Trainers")
    print("(3)coordinador")
    print("(4)finalizar programa")
    op=input("que tipo de personas eres: ")

    if op=="1":
        print("=======Menu campers======")
        print("(1)mostrar datos del campers\n (2)volver al menu principal")



    elif op=="2":
        variable=True
        while variable==True:

            lisTrainer=[]
            print("============menu Trainers==============")
            print("(1)verificar informacion del trainer\n (2)volver al menu principal ")
            opcion=input("Ingrese la opcion deseada")
            
            n=int(input("ingrese tu id para ver tus datos"))
            if opcion=="1":
                lisTrainer= mostrarTrainers()
                for i in lisTrainer[n]["trainer"]:
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Horario:",i["Horario"])
                    print("ruta",i["ruta"])
            if opcion=="2":
                print("Se volvio al menu principal")
                variable=False
            


    elif op=="3":
        print("=============Menu coordinador===========")
        print("(1)ver cantidad de campers en estado de inscripcion\n(2)ver trainers trabajando en campus\n(3)Añadir nuevo campers \n(4) asignar notas a los campers \n(5)Asignar las rutas de entrenamiento a los campers\n (6)Crear nuevas rutas de entrenamiento(7)asignar los trainers encargados de cada ruta")
        opc=input("Ingrese la opcion deseada: ")

        if opc=="1":#opcion para mostrar los campers que se inscribieron 
            print("Los campers en estado de inscripcion son: ")
            datosCampers=[]
            datosCampers= mostrarCampers()
            campersInscritos=[]
            campersReprobados=[]
            print(datosCampers)
            for camper in datosCampers["campers"]:
                if camper["estado"] == "Inscrito":
                    campersInscritos.append(camper)
                else:
                    campersReprobados.append(camper)
            print(campersInscritos)
            


        elif opc=="2":#opcion para mostrar la lista de Trainers que trabajan en campusland
            print("Los trainers que trabajan en campuslands son: ")
            contador=0
            lisTrainer=[]
            lisTrainer= mostrarTrainers()
            cantidadTrainers= len(lisTrainer)
            print(cantidadTrainers)
            for i in lisTrainer[0]["trainer"]:#falta solucionar error para que imprima todos los Trainer del Json
                contador+=1
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Horario:",i["Horario"])
                print("ruta",i["ruta"])
            print("La cantidad de Trainers trabajando en campuslands son:", cantidadTrainers)


        elif opc=="3":#opcion para añadir nuevos campers 
            print("Ingrese los datos para el nuevo camper")
            nuevoCamper=[]
            nuevoCamper= mostrarCampers()
            crearCamper={}
            crearCamper["id"]=input("Ingrese el nuevo id del camper")
            crearCamper["nombre"]=input("ingrese el nombre del camper: ")
            crearCamper["apellidos"]=input("Ingrese el apellido del camper: ")
            crearCamper["direccion"]=input("Ingresa la dirreccion del campers: ")
            crearCamper["acudiente"]=input("ingrese el nombre del acudiente: ")
            crearCamper["celular"]=input("Ingrese el numero del telefono celular: ")
            crearCamper["fijo"]=input("Ingrese el numero de telefono fijo: ")
            crearCamper["estado"]=input("ingrese el estado en el que se encuentra el camper: ")
            crearCamper["riesgo"]=input("Ingrese el riesgo en el que se encuentra el camper: ")
            crearCamper["ruta"]=input("Ingresa la ruta que va a seguir el campers: ")
            
            n=input("En que grupo desea agregar al nuevo campers se encuentran los grupos: (0)=T1, (1)=T2, (2)=T3: ")
            nuevoCamper[n]["campers"].append(crearCamper)# falta solucionar error para incorporar al acmper al grupo deseado por el usuario
            guardarArchivo(nuevoCamper)
            print("Se agrego correctamente al nuevo campers")



        elif opc=="4":# opcion para saber si los campers aprueban o no los modulos 
            print("Ingrese las notas de los campers")


        elif opc=="5":#opcion para asignar los modulos a cada campers
            print("Asigne las rutas a los campers")

        elif opc=="6": #opcion para crear nuevos modulos de entrenamiento
            print("cree nuevas rutas o modulos de entrenamiento")

        elif opc=="7":#opcion para asignar los trainers a cada ruta
            print("Asigne los Trainers que van a estar encargados de cada ruta")






