

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
        print("============menu Trainers==============")
        print("(1)verificar informacion del trainer\n (2)volver al menu principal ")

    elif op=="3":
        print("=============Menu coordinador===========")
        print("(1)ver cantidad de campers en estado de inscripcion\n (2)ver trainers trabajando en campus \n(3) asignar notas a los campers \n(4)Asignar las rutas a los campers\n (5)asignar las aulas encargadas de cada trainers")

