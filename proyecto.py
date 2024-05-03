
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
                lisCampers=[]
                lisCampers=mostrarCampers()
                
                id=int(input("ingrese tu id para ver tu informacion: "))
                for grupo in lisCampers:
                        for camper in grupo["campers"]:
                            if camper["id"]==id:
                                print("ID",camper["id"])
                                print("Nombres:",camper["nombres"])
                                print("Apellidos:",camper["apellidos"])
                                print("ruta",camper["ruta"])
                                print("estado"),camper["estado"]
                                print("modulos:")
                                for modulo in camper["modulos"]:
                                    print("modulo", modulo,"estado:", camper["modulos"][modulo])
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
                n=n-1# se le resto un punto ya que inicia el conteo apartir de cero
                lisTrainer= mostrarTrainers()
                for i in lisTrainer[n]["trainer"]:
                    print("ID",i["id"])
                    print("Nombre:",i["nombre"])
                    print("Apellido:",i["apellido"])
                    print("Horario:",i["Horario"])
                    print("ruta",i["ruta"])
                    print("grupo",i["grupo"])
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
        print("(1)Añadir nuevo campers\n(2)asignar notas a los campers\n(3)Asignar las rutas de entrenamiento a los campers\n(4)Crear nuevas rutas de entrenamiento\n(5)asignar los trainers encargados de cada ruta\n(6)realizar reportes")
        opc=input("Ingrese la opcion deseada: ")

        if opc=="1":#opcion para añadir un nuevo campers
            print("Opcion para añadir nuevos campers")
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
            nuevoCamper[n]["campers"].append(crearCamper)
            guardarArchivoCampers(nuevoCamper)
            print("Se agrego correctamente al nuevo campers")


        elif opc=="2":#opcion para asignar las notas a los campers
            print("La nota de los campers son: ")


        elif opc=="3":#opcion para asignar las rutas de entrenamiento a los campers
            print()



        elif opc=="4":# opcion para Crear nuevas rutas de entrenamiento
            print("Ingrese")
            print("cree nuevas rutas o modulos de entrenamiento")
            diccionario_rutas={}# se crea un diccionario vacio para añadir los modulos
            diccionario_rutas.update({"programacion formal":"Java, JavaScript, c#", "bases de datos":"Mysql, mongoDb, Postgresql", "backend": "NetCore, Spring Boot, NodeJs, Express"})
            print(diccionario_rutas)
            print("A que ruta le quieres añadir mas modulos")
            print("(1)Ruta NodeJS\n(2)Ruta Java\n(3)Ruta NetCore")
            id=int(input("Ingrese la opcion deseada: "))
            listaRutass=[]
            listaRutass=mostrarRutas()
            bucleRuta=True
            while bucleRuta==True:# se crea un bucle para ver si el coordinador quiere seguir asignando rutas a los trainers
                bucl=True
                while bucl==True:
                    for dato in listaRutass:
                        for rutas in ["modulos"]:
                            if  rutas["id"]==id:
                                modulo=input("Ingrese el modulo que le va a asignar a la ruta: ")
                                rutas["modulos"]= modulo
                                guardarArchivoRutas(listaRutass)
                                print("modulos asignados correctamente")
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






        elif opc=="5":#opcion asignar los trainers encargados de cada ruta
            print("Asigne las rutas a los trainers")
            lisTrainer=[]
            lisTrainer= mostrarTrainers()
            print()
            bucleTrainer=True
            bu=True
            
            while bucleTrainer==True:# se crea un bucle para ver si el coordinador quiere seguir asignando rutas a los trainers
                bucl=True
                while bucl==True:
                    id=int(input("Ingrese el ID del trainer al cual le vas a asignar la ruta: "))
                    
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
            
            
        elif opc=="6":# opcion para hacer un reporte
            print("Opcion de Reporte")
            print("##########################################")
            print("========Menu de opciones Reportes=========")
            print("##########################################")
            print("(1)Listar los **campers** que se encuentren en estado de inscrito.")# opcion realizada correctamente
            print("(2)Listar los **campers** que aprobaron el examen inicial.")
            print("(3)Listar los entrenadores que se encuentran trabajando con **CampusLands**.")#opcion realizada correctamente
            print("(4)Listar los **campers** que cuentan con bajo rendimiento.")
            print("(5)Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.")
            print("(6)Mostrar cuantos **campers** perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
            respuesta=input("Ingrese la opcion deseada")


            if respuesta=="1":
                print("Los campers en estado de inscrito son: ")
                datosCampers= mostrarCampers()
                campersInscritos=[]# se crea una lista para separar a los campers que pasaron la inscipcion
                
                for grupo in datosCampers:
                        
                        for campe in grupo["campers"]:
                            if campe["estado"]=="Inscrito":
                                campersInscritos.append(campe)
                cantidadCampers= len(campersInscritos)
                for i in campersInscritos:
                    print("ID:",i["id"])
                    print("Nombre:",i["nombres"])
                    print("Apellido:",i["apellidos"])
                    print("direccion:",i["direccion"])
                    print("acudiente",i["acudiente"])
                    print("estado",i["estado"])
                print("La cantidad de campers inscritos son: ",cantidadCampers)




            elif respuesta=="3":
                print("Los trainers que trabajan en campuslands son: ")
                
                lisTrainer= mostrarTrainers()
                cantidadTrainers= len(lisTrainer)# se cuenta la cantidad de trainers que hay en el json
                for trainer in lisTrainer:
                        posicion=trainer["trainer"][0]# se imprimen los trainers desde la pocicion 0
                        print("Nombre:",posicion["nombre"])
                        print("Apellido:",posicion["apellido"])
                        print("Horario:",posicion["Horario"])
                        print("ruta",posicion["ruta"])
                        print("grupo",posicion["grupo"])
                        print()
                print("La cantidad de Trainers trabajando en campuslands son:", cantidadTrainers)



            elif respuesta=="4":
                print("los campers con bajo rendimiento son: ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    elif op=="4":# opcion para finalizar el bucle principal
        print("Gracias por participar hasta luego...")
        buclePrincipal=False

# falta hacer los calculos de los horarios para designar cuantos Trainers son necesarios para las rutas 
#falta designar el inicio y el final de cada ruta osea cuando inicia el programa de esa ruta y cuando finaliza ese programa




