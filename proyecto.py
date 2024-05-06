
#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def mostrarTrainers():# se crea una funcion para ver o extraer el contenido del Json
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
def mostrarCampers():# se crea una funcion para ver o extraer el contenido del Json
    listaCampers=[]
    with open('Campers.json','r') as openfile:
        listaCampers= json.load(openfile)

    return listaCampers

def guardarArchivoCampers(miData):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Campers.json","w") as outfile:
        json.dump(miData,outfile)









#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
def mostrarRutas():# se crea una funcion para ver o extraer el contenido del Json
    listaRutas=[]
    with open('rutas.json','rb') as openfile:
        listaRutas= json.load(openfile)

    return listaRutas
def guardarArchivoRutas(miDato1):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("rutas.json","w") as outfile:
        json.dump(miDato1,outfile)


def calcularEstadoCampers(total_score):
    if total_score>=60:
        return "Aprobado"
    else:
        return "Reprobado"


buclePrincipal=True
while buclePrincipal==True:
    print("##########################################")
    print("======== MENU PRINCIPAL DE OPCIONES ========")
    print("##########################################")
    print("(1) campers")
    print("(2)Trainers")
    print("(3)coordinador")
    print("(4)finalizar programa")
    op=input("Ingresa la opcion deseada: ")

    if op=="1":
        buli=True
        while buli==True:
            print("##########################################")
            print("================ Menu campers ==============")
            print("##########################################")
            print("(1) Mostrar mis datos como campers\n(2) volver al menu principal")
            opcion=input("Ingrese la opcion deseada: ")
                
            if opcion=="1":
                lisCampers=[]
                lisCampers=mostrarCampers()
                
                id=int(input("ingresa tu id para ver tu informacion: "))
                for grupo in lisCampers:
                        for camper in grupo["campers"]:
                            if camper["id"]==id:
                                print("ID",camper["id"])
                                print("Nombres:",camper["nombres"])
                                print("Apellidos:",camper["apellidos"])
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
                bucleReportes=True
                while bucleReportes==True:

                    print("Opcion de Reporte")
                    print("##########################################")
                    print("========Menu de opciones Reportes=========")
                    print("##########################################")
                    print("(1)Listar los **campers** que se encuentren en estado de inscrito.")
                    print("(2)Listar los **campers** que aprobaron el examen inicial.")
                    print("(3)Listar los entrenadores que se encuentran trabajando con **CampusLands**.")
                    print("(4)Listar los **campers** que cuentan con bajo rendimiento.")
                    print("(5)Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.")
                    print("(6)Mostrar cuantos **campers** perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
                    print("(7)volver al menu principal")
                    respuesta=input("Ingrese la opcion deseada: ")


                    if respuesta=="1":
                        print("=====================================")
                        print("Los campers en estado de inscrito son: ")
                        print("=====================================")
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


                    elif respuesta=="2":# opcion para Listar los **campers** que aprobaron el examen inicial
                        print("================================================")
                        print("Los campers que aprobaron el examen inicial son:")
                        print("================================================")
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
                        print("La cantidad de campers que aprobaron el examen inicial son: ",cantidadCampers)




                    elif respuesta=="3":#opcion para listar los trainers que trabajan en campusland 
                        print("==============================================")
                        print("Los trainers que trabajan en campuslands son: ")
                        print("==============================================")
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
                        print("=======================================")
                        print("los campers con bajo rendimiento son: ")
                        print("=======================================")
                        datosCampers= mostrarCampers()
                        campersRendimientoBajo=[]# se crea una lista para separar a los campers con bajo rendimiento

                        for grupo in datosCampers:
                                
                                for campe in grupo["campers"]:
                                    if campe["riesgo"]=="Bajo":
                                        campersRendimientoBajo.append(campe)
                        cantidadCampers= len(campersRendimientoBajo)
                        for i in campersRendimientoBajo:
                            print("ID:",i["id"])
                            print("Nombre:",i["nombres"])
                            print("Apellido:",i["apellidos"])
                            print("direccion:",i["direccion"])
                            print("acudiente",i["acudiente"])
                            print("riesgo",i["riesgo"])
                        print("La cantidad de campers con bajo rendimiento son: ",cantidadCampers)
                    
                    elif respuesta=="5":
                        print("===========================================================================================")
                        print("los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento son:")
                        print("===========================================================================================")
                        print()
                        print("=====================================")
                        print("Los campers asociados a una ruta son: ")
                        print("=====================================")
                        datosCampers= mostrarCampers()
                        campersInscritos=[]# se crea una lista para separar a los campers que pasaron la inscipcion
                        
                        for grupo in datosCampers:
                                
                                for campe in grupo["campers"]:
                                    if campe["estado"]=="Aprobado":
                                        campersInscritos.append(campe)
                        cantidadCampers= len(campersInscritos)
                        for i in campersInscritos:
                            print("ID:",i["id"])
                            print("Nombre:",i["nombres"])
                            print("Apellido:",i["apellidos"])
                            print("direccion:",i["direccion"])
                            print("acudiente",i["acudiente"])
                            print("estado",i["estado"])
                        print("La cantidad de campers asociados a una ruta son: ",cantidadCampers)
                        print()
                        print("======================================")
                        print("LOS TRAINERS ASOCIADOS A UNA RUTA SON:")
                        print("======================================")
                        lisTrainer= mostrarTrainers()
                        trainersRutas=[]
                        for trainerr in lisTrainer:
                            for trainer in trainerr["trainer"]:
                                if trainer["ruta"]!="No asignada":
                                    trainersRutas.append(trainer)
                        cantidadTrainers=len(trainersRutas)
                        for posicion in trainersRutas:
                                    
                            print("Nombre:",posicion["nombre"])
                            print("Apellido:",posicion["apellido"])
                            print("Horario:",posicion["Horario"])
                            print("ruta",posicion["ruta"])
                            print("grupo",posicion["grupo"])
                            print()
                        print("La cantidad de Trainers que se encuentran asociados a una ruta de entrenamiento son: ",cantidadTrainers)
                    
                    elif respuesta == "7":
                        print("Se volvio al menu principal")
                        bucleReportes=False
                    else:
                        print("===================================")
                        print("Porfavor ingrese una opcion valida")
                        print("===================================")



            elif opcion=="3":
                print("Se volvio al menu principal")
                variable=False
            else:
                print("Porfavor ingrese una opcion valida")
            


    elif op=="3":
        bucleCoordinador=True
        while bucleCoordinador==True:
            print("##########################################")
            print("============= Menu coordinador ===========")
            print("##########################################")
            print("(1) Agregar nota del examen de ingreso\n(2) Añadir nuevo campers\n(3) Asignar notas a los campers\n(4) Asignar las rutas de entrenamiento a los grupos\n(5) Crear nuevas rutas\n(6) Asignar los trainers encargados de cada ruta\n(7) Realizar reportes\n(8) Salir al menu principal")
            opc=input("Ingrese la opcion deseada: ")

            if opc == "1": # Falta coregir esta opcion
                campers = mostrarCampers()
                grupo_canmper = input("ingresa el grupo en el que el camper se encuetra asignado: ")
                camper_id = int(input("Ingrese el ID del camper: "))
                for grupo in campers:
                    if grupo["grupo"]==grupo_canmper:
                        for camper in grupo["campers"]:
                            if camper["id"]==camper_id:
                                    modulo = input("Ingrese el nombre del módulo: ")
                                    nota_teorica = float(input("Ingrese la nota teórica: "))
                                    nota_practica = float(input("Ingrese la nota práctica: "))
                                    nota_taller1 = float(input("ingresa la nota del taller 1: "))
                                    nota_taller2 = float(input("ingresa la nota del taller 2: "))
                                    camper["modulos"][modulo]={
                                        "nota_teorica": nota_teorica,
                                        "nota_practica": nota_practica,
                                        "nota_taller1": nota_taller1,
                                        "nota_taller2": nota_taller2
                                    }
                                    
                                    tatal_score=nota_teorica*0.3 + nota_practica*0.6+nota_taller1*0.05+nota_taller2*0.05
                                    camper["estado"]= calcularEstadoCampers
                                    guardarArchivoCampers(campers)
                                    print("nota guardada correctamente")
                                    
                            else:
                                continue
                            break
                    else:
                        print("camper no encontrado")
                    

            elif opc=="2":#opcion para añadir un nuevo campers
                print("Opcion para añadir nuevos campers")
                print("Ingrese los datos para el nuevo camper")
                nuevoCamper= mostrarCampers()
                crearCamper={}
                crearCamper["id"]=int(input("Ingrese el nuevo id del camper: "))
                crearCamper["nombres"]=input("ingrese el nombre del camper: ")
                crearCamper["apellidos"]=input("Ingrese el apellido del camper: ")
                crearCamper["direccion"]=input("Ingresa la dirreccion del campers: ")
                crearCamper["acudiente"]=input("ingrese el nombre del acudiente: ")
                crearCamper["telefonos"]={"celular": input("Ingrese el numero del telefono celular: "),"fijo":input("Ingrese el numero del telefono fijo: ")}
                crearCamper["estado"]=input("ingrese el estado en el que se encuentra el camper: ")
                crearCamper["riesgo"]=input("Ingrese el riesgo de desercion en el que se encuentra el camper: ")
                crearCamper["modulos"]={"modulo1":input("Ingrese la nota del modulo1 si ya lo completo si no presione ENTER: "),"modulo2": input("Ingrese la nota del modulo2 si ya lo completo si no presione ENTER: "), "modulo3": input("Ingrese la nota del modulo3 si ya lo completo si no presione ENTER: ")}
                
                n=int(input("En que grupo desea agregar al nuevo campers se encuentran los grupos: (0)=T1, (1)=T2, (2)=T3: "))
                nuevoCamper[n]["campers"].append(crearCamper)
                guardarArchivoCampers(nuevoCamper)
                print("Se agrego correctamente al nuevo campers")


            elif opc=="3":#opcion para asignar las notas a los campers
                grupo=input("Ingrese el id del camper al cual le vas a asignar la nota: ")
                



            elif opc=="4":#opcion para asignar las rutas de entrenamiento de los grupos
                listaaCamper=[]
                listaaCamper= mostrarCampers()
                bucleRutas=True
                bu=True
                
                while bucleRutas==True:# se crea un bucle para ver si el coordinador quiere seguir asignando rutas a los trainers
                    bucl=True
                    while bucl==True:
                        grupo=input("Ingrese el nombre del grupo al cual le vas a asignar la ruta ")
                        ruta=input("Ingrese la ruta que le va a asignar al grupo: ")
                        for grupo in listaaCamper:
                            if grupo["grupo"]==grupo:
                                grupo["ruta"]=ruta
                                guardarArchivoCampers(listaaCamper)
                                print()
                                bu=True
                                bucl=False
                                print("Ruta asignada correctamente al grupo")
                        while bu==True:
                            print("desea terminar de asignar las rutas (si) o (no)")
                            res=input()
                            if res=="si":
                                print("se finalizo la asignacion de las rutas a los Grupos")
                                bucleRutas=False
                                bu=False
                                bucl=False
                            elif res=="no":
                                bu=False
                                print("continue asignandole las rutas a los grupos")
                            else:
                                print("Porfavor ingrese una opcion valida ")



            elif opc=="5":# opcion para Crear nuevas rutas de entrenamiento 
                print("Ingrese los datos para la nueva ruta de entrenamiento")
                nuevasRutas = mostrarRutas()
                crearRuta={}
                crearRuta["id"]=len (nuevasRutas[0]["ruta"])+1
                crearRuta["ruta"]=input("ingrese la nombre de la nueva ruta: ")
                crearRuta["Trainers"]=input("Ingrese el nombre del Trainer encargado de esta ruta: ")
                crearRuta["fechaInicio"]=input("Ingrese la fecha de inicio de esta ruta: ")
                crearRuta["fechaFin"]=input("ingrese la fecha final de esta ruta : ")
                print("Las materias disponibles para cada modulo son: )")
                print("- Fundamentos de programación MATERIAS:(Introducción a la algoritmia, PSeInt y Python)")
                print("- Programación Web MATERIAS:(HTML, CSS y Bootstrap)")
                print("- Programación formal MATERIAS:(Java, JavaScript, C#)")
                print("- Bases de datos MATERIAS:(Mysql, MongoDb y Postgresql)")
                print("- Backend MATERIAS:(NetCore, Spring Boot, NodeJS y Express)")
                crearRuta["modulos"]={"Fundamentos_de_ programación": input("Ingrese las materias requeridas del modulo Fundamentos_de_ programación: "),"Programación Web":input("Ingrese las materias requeridas del modulo Programación Web: "),"Programación formal": input("Ingrese las materias requeridas del modulo Programación formal: "),"Bases de datos": input("ingrese las materias requeridas del modulo Bases de datos: "),"Backend":input("Ingrese las materias requeridas del modulo Backend: ")}
                nuevasRutas.append(crearRuta)
                guardarArchivoRutas(nuevasRutas)
                print("Se agrego correctamente la nueva ruta")
                








            elif opc=="6":#opcion asignar los trainers encargados de cada ruta
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
                
                
            elif opc=="7":# opcion para reportes
                bucleReportes=True
                while bucleReportes==True:

                    print("Opcion de Reporte")
                    print("##########################################")
                    print("========Menu de opciones Reportes=========")
                    print("##########################################")
                    print("(1)Listar los **campers** que se encuentren en estado de inscrito.")
                    print("(2)Listar los **campers** que aprobaron el examen inicial.")
                    print("(3)Listar los entrenadores que se encuentran trabajando con **CampusLands**.")
                    print("(4)Listar los **campers** que cuentan con bajo rendimiento.")
                    print("(5)Listar los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento.")
                    print("(6)Mostrar cuantos **campers** perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
                    print("(7)volver al menu principal")
                    respuesta=input("Ingrese la opcion deseada")


                    if respuesta=="1":
                        print("=====================================")
                        print("Los campers en estado de inscrito son: ")
                        print("=====================================")
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


                    elif respuesta=="2":# opcion para Listar los **campers** que aprobaron el examen inicial
                        print("================================================")
                        print("Los campers que aprobaron el examen inicial son:")
                        print("================================================")
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
                        print("La cantidad de campers que aprobaron el examen inicial son: ",cantidadCampers)




                    elif respuesta=="3":#opcion para listar los trainers que trabajan en campusland 
                        print("==============================================")
                        print("Los trainers que trabajan en campuslands son: ")
                        print("==============================================")
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
                        print("=======================================")
                        print("los campers con bajo rendimiento son: ")
                        print("=======================================")
                        datosCampers= mostrarCampers()
                        campersRendimientoBajo=[]# se crea una lista para separar a los campers con bajo rendimiento

                        for grupo in datosCampers:
                                
                                for campe in grupo["campers"]:
                                    if campe["riesgo"]=="Bajo":
                                        campersRendimientoBajo.append(campe)
                        cantidadCampers= len(campersRendimientoBajo)
                        for i in campersRendimientoBajo:
                            print("ID:",i["id"])
                            print("Nombre:",i["nombres"])
                            print("Apellido:",i["apellidos"])
                            print("direccion:",i["direccion"])
                            print("acudiente",i["acudiente"])
                            print("riesgo",i["riesgo"])
                        print("La cantidad de campers con bajo rendimiento son: ",cantidadCampers)
                    
                    elif respuesta=="5":
                        print("===========================================================================================")
                        print("los **campers** y **trainers** que se encuentren asociados a una ruta de entrenamiento son:")
                        print("===========================================================================================")
                        print()
                        print("=====================================")
                        print("Los campers asociados a una ruta son: ")
                        print("=====================================")
                        datosCampers= mostrarCampers()
                        campersInscritos=[]# se crea una lista para separar a los campers que pasaron la inscipcion
                        
                        for grupo in datosCampers:
                                
                                for campe in grupo["campers"]:
                                    if campe["estado"]=="Aprobado":
                                        campersInscritos.append(campe)
                        cantidadCampers= len(campersInscritos)
                        for i in campersInscritos:
                            print("ID:",i["id"])
                            print("Nombre:",i["nombres"])
                            print("Apellido:",i["apellidos"])
                            print("direccion:",i["direccion"])
                            print("acudiente",i["acudiente"])
                            print("estado",i["estado"])
                        print("La cantidad de campers asociados a una ruta son: ",cantidadCampers)
                        print()
                        print("======================================")
                        print("LOS TRAINERS ASOCIADOS A UNA RUTA SON:")
                        print("======================================")
                        lisTrainer= mostrarTrainers()
                        trainersRutas=[]
                        for trainerr in lisTrainer:
                            for trainer in trainerr["trainer"]:
                                if trainer["ruta"]!="No asignada":
                                    trainersRutas.append(trainer)
                        cantidadTrainers=len(trainersRutas)
                        for posicion in trainersRutas:
                                    
                            print("Nombre:",posicion["nombre"])
                            print("Apellido:",posicion["apellido"])
                            print("Horario:",posicion["Horario"])
                            print("ruta",posicion["ruta"])
                            print("grupo",posicion["grupo"])
                            print()
                        print("La cantidad de Trainers que se encuentran asociados a una ruta de entrenamiento son: ",cantidadTrainers)

                    elif respuesta=="6":
                        print("Los **campers** que  perdieron y aprobaron cada uno de los módulos son: ")
                        datosCampers= mostrarCampers()
                        campersInscritos=[]# se crea una lista para separar a los campers que pasaron la inscipcion
                        print("=====================================")
                        print("Los campers que perdieron modulos son: ")
                        print("=====================================")
                        
                        for grupo in datosCampers:
                                
                                for campe in grupo["campers"]:
                                    if campe["estado"]=="Reprobado":
                                        campersInscritos.append(campe)
                        cantidadCampers= len(campersInscritos)
                        for i in campersInscritos:
                            print("ID:",i["id"])
                            print("Nombre:",i["nombres"])
                            print("Apellido:",i["apellidos"])
                            print("direccion:",i["direccion"])
                            print("acudiente",i["acudiente"])
                            print("estado",i["estado"])
                        print("La cantidad de campers asociados a una ruta son: ",cantidadCampers)
                        print()
                    
                    elif respuesta == "7":# opcion para finalizar el bucle de los reportes
                        print("Se volvio al menu principal")
                        bucleReportes=False
                    else:
                        print("Porfavor ingrese una opcion valida")

            elif opc=="8":#opcion para finalizar el bucle del trainer
                print("Se volvio al menu principal")
                bucleCoordinador=False
            else:
                print("===================================")
                print("Porfavor ingrese una opcion valida")
                print("===================================")

    
    
    
    
    
    
    
    
    
    
    
    
    
    elif op=="4":# opcion para finalizar el bucle principal
        print("Gracias por participar hasta luego...")
        buclePrincipal=False
    else:
        print("===================================")
        print("Porfavor ingrese una opcion valida")
        print("===================================")






