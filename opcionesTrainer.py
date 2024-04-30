def calcular_notas(cantidad_notas, notas):
    if cantidad_notas!= len(notas):
        raise ValueError(" la cantidad de notas y listas de notan deben tener la misma cantidad dada")
    
    promedio=sum(notas)/ cantidad_notas
    return promedio

cantidad_notas= 4
notas=[float(input("ingresa notas {}: ".format(i+1)))for i in range(cantidad_notas)]
promedio= calcular_notas(cantidad_notas, notas)
print("el promdedio de las notas es: ", int(promedio))

nota1=input("Ingrese la nota de la  prueba teórica: ")
nota2=input("Ingrese la nota de la prueba practica: ")
nota3=input("Ingrese la nota de del primer taller")
nota4=input("ingrese la nota del segundo taller ")
notaFinal=(nota1*0.3)+(nota2*0.6)+(nota3*0.05)+(nota4*0.05)/4

