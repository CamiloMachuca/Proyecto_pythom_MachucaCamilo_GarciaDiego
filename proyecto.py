
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

def guardarArchivoRutas(miDato1):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("rutas.json","w") as outfile:
        json.dump(miDato1,outfile)





import json
# funcion para mostrar los datos del Json
def mostrarRutas():
    listaRutas=[]
    with open('rutas.json','r') as openfile:
        listaRutas= json.load(openfile)

    return listaRutas









buclePrincipal=True
while buclePrincipal==True:
    print("##########################################")
    print("======== MENU PRINCIPAL DE OPCIONES =========")
    print("##########################################")
    print("(1) campers")# opcion realizada 
    print("(2)Trainers")# opcion realizada
    print("(3)coordinador")
    print("(4)finalizar programa")
    op=input("que opcion eliges: ")

    if op=="1":
        buli=True
        while buli==True:
            print("##########################################")
            print("================ Menu campers ==============")
            print("##########################################")
            print("(1)mostrar datos del campers\n(2)volver al menu principal")
            opcion=input("Ingrese la opcion deseada: ")
                
            if opcion=="1":
               
                lisCampers= mostrarCampers()# programa para mostrar campersss
                print(lisCampers)
                for i in lisCampers[0]["campers"]:
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Horario:",i["Horario"])
                    print("ruta",i["ruta"])
            if opcion=="2":
                print("Se volvio al menu principal")
                buli=False
            else:
                print("Porfavor ingrese una opcion valida")



    elif op=="2":
        variable=True
        while variable==True:

            lisTrainer=[]
            print("##########################################")
            print("============= menu Trainers ==============")
            print("##########################################")
            print("(1)verificar informacion del trainer\n(2)Reportes\n(3)volver al menu principal ")
            opcion=input("Ingrese la opcion deseada")
            
            
            if opcion=="1":
                n=int(input("ingrese tu id para ver tus datos"))
                lisTrainer= mostrarTrainers()
                for i in lisTrainer[n]["trainer"]:
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Horario:",i["Horario"])
                    print("ruta",i["ruta"])
                    print("salon",i["salon"])
            elif opcion=="2":
                print("opcion de reportes")



            elif opcion=="3":
                print("Se volvio al menu principal")
                variable=False
            else:
                print("Porfavor ingrese una opcion valida")
            


    elif op=="3":
        print("##########################################")
        print("============= Menu coordinador ===========")
        print("##########################################")
        print("(1)ver cantidad de campers en estado de inscripcion\n(2)ver trainers trabajando en campus\n(3)Añadir nuevo campers \n(4)asignar notas a los campers \n(5)Asignar las rutas de entrenamiento a los campers\n(6)Crear nuevas rutas de entrenamiento\n(7)asignar los trainers encargados de cada ruta\n(8)reportes")
        opc=input("Ingrese la opcion deseada: ")

        if opc=="1":#opcion para mostrar los campers que se inscribieron 
            print("Los campers en estado de inscripcion son: ")
            datosCampers=[]
            datosCampers= mostrarCampers()
            campersInscritos=[]# se crea una lista para separar a los campers que pasaron la inscipcion
            
            for grupo in datosCampers["grupos"][0]:
                    for campe in grupo["campers"]:
                        if  "estado" in campe["camper"] and campe["camper"]["estado"]=="Inscrito":

                            campersInscritos.append(campe["camper"])# falta solucionar porque se estan repitiendo los nombres de unos campers
                            cantidadCampers= len(campersInscritos)
                            for i in campersInscritos:
                                print("ID:",i["id"])
                                print("Nombre:",i["nombres"])
                                print("Apellido:",i["apellidos"])
                                print("direccion:",i["direccion"])
                                print("acudiente",i["acudiente"])
                                print("acudiente",i["acudiente"])
                                print()
            print("La cantidad de campers inscritos son: ",cantidadCampers)
            
            #for camper in datosCampers:# falta solucionar error para seleccionar los campers que en el estada aparesca: aprobado
               # if camper['estado']== "Inscrito":
                   # campersInscritos.append(camper)
                   # print(campersInscritos)               
            


        elif opc=="2":#opcion para mostrar la lista de Trainers que trabajan en campusland
            print("Los trainers que trabajan en campuslands son: ")
            lisTrainer=[]
            lisTrainer= mostrarTrainers()
            cantidadTrainers= len(lisTrainer)# se cuenta la cantidad de trainers que hay en el json
            print(cantidadTrainers)
            for i in lisTrainer[0]["trainer"]:#falta solucionar error para que imprima todos los Trainer del Json
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Horario:",i["Horario"])
                print("ruta",i["ruta"])
            print("La cantidad de Trainers trabajando en campuslands son:", cantidadTrainers)


        elif opc=="3":#opcion para añadir nuevos campers 
            print("Ingrese los datos para el nuevo camper")
            nuevoCamper= mostrarCampers()
            crearCamper={}
            crearCamper["id"]=input("Ingrese el nuevo id del camper")
            crearCamper["nombres"]=input("ingrese el nombre del camper: ")
            crearCamper["apellidos"]=input("Ingrese el apellido del camper: ")
            crearCamper["direccion"]=input("Ingresa la dirreccion del campers: ")
            crearCamper["acudiente"]=input("ingrese el nombre del acudiente: ")
            crearCamper["telefonos"]={"celular": input("Ingrese el numero del telefono celular: "),"fijo":input("Ingrese el numero del telefono fijo: ")}
            crearCamper["estado"]=input("ingrese el estado en el que se encuentra el camper: ")
            crearCamper["riesgo"]=input("Ingrese el riesgo en el que se encuentra el camper: ")
            crearCamper["ruta"]=input("Ingresa la ruta que va a seguir el campers: ")
            
            n=int(input("En que grupo desea agregar al nuevo campers se encuentran los grupos: (0)=T1, (1)=T2, (2)=T3: "))
            nuevoCamper["grupos"][n]["campers"].append({"camper":crearCamper})# falta solucionar error para incorporar al camper al grupo deseado por el usuario error resuelto falta probar todos los grupos
            guardarArchivoCampers(nuevoCamper)
            print("Se agrego correctamente al nuevo campers")



        elif opc=="4":# opcion para saber si los campers aprueban o no los modulos 
            print("Ingrese las notas de los campers")






        elif opc=="5":#opcion para asignar los modulos a cada campers SABIENDO QUE ESTOS CAMPERS YA PASARON LA PREUBA DE INGRESO 
            print("Asigne las rutas a los campers")





        elif opc=="6": #opcion para añadir nuevos modulos a las rutas de entrenamiento
            print("cree nuevas rutas o modulos de entrenamiento")
            diccionario_rutas={}# se crea un diccionario vacio para añadir los modulos
            diccionario_rutas.update({"programacion formal":"Java, JavaScript, c#", "bases de datos":"Mysql, mongoDb, Postgresql", "backend": "NetCore, Spring Boot, NodeJs, Express"})
            print(diccionario_rutas)
            print("A que ruta le quieres añadir mas modulos")
            print("(1)Ruta NodeJS\n(2)Ruta Java\n(3)Ruta NetCore")
            Añadir_ruta=input("ingrese la opcion de la ruta a la cual le vas a añadir mas modulos: ")
            if Añadir_ruta=="1":
                print("ruta NodeJS")#falta programa para añadir los modulos a la ruta NodeJS
                print()


            elif Añadir_ruta=="2":
                print("ruta java")#Falta programa para añadir los modulos a la ruta java


            elif Añadir_ruta=="3":#falta programa para añadir los modulos a la ruta Netcore
                print("ruta NetCore")





        elif opc=="7":#opcion para asignar los trainers a cada ruta
            
            lisTrainer=[]
            lisTrainer= mostrarTrainers()
            print("Asigne los Trainers que van a estar encargados de cada ruta")
            print()
            #n=int(input("ingrese el id del trainer al cual le vas a asignar la ruta "))
            bucleTrainer=True
            bu=True
            
            while bucleTrainer==True:# se crea un bucle para ver si el coordinador quiere seguir asignando rutas a los trainers
                bucl=True
                while bucl==True:
                    id=int(input("Ingrese el nombre del trainer al cual le vas a asignar la ruta: "))
                    
                    for dato in lisTrainer:
                        for trainers in dato["trainer"]:
                            if  trainers["id"]==id:
                                ruta=input("Ingrese la ruta que le va a asignar al trainer: ")
                                trainers["ruta"]= ruta
                                guardarArchivoTrainers(lisTrainer)
                                print("Ruta asignada correctamente")
                                print()
                                bu=True
                                bucl=False


                    while bu==True:
                        print("desea terminar de asignar las rutas (si) o (no)")
                        res=input()
                        if res=="si":
                            print("se finalizo la asignacion de las rutas a los Trainers")
                            bucleTrainer=False
                            bu=False
                            bucl=False
                        elif res=="no":
                            bu=False
                            print("continue asignandole las rutas a los trainers ")
                        else:
                            print("Porfavor ingrese una opcion valida ")

# falta hacer los calculos de los horarios para designar cuantos Trainers son necesarios para las rutas 
#falta designar el inicio y el final de cada ruta osea cuando inicia el programa de esa ruta y cuando finaliza ese programa




