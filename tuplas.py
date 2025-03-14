#Programa para recordar tuplas
#milista = ["daniel", "daniel2", "daniel3", "daniel4"]
#acceder a la posicion 3: milista[3], se guarda daniel3 y asi sucesivamente
import os          #limpiar
os.system('cls')   #limpiar

mitupla = ("daniel", 7, "daniel3", 12)
print(mitupla[3]) #imprimir el elemento del indice 3

#convertir una tupla en lista 
milista=list(mitupla)
print(mitupla)

#convertir una lista tupla en una tupla
milista = ["daniel", "daniel2", "daniel", "daniel4", "daniel"]
mitupla = tuple(milista)
print(mitupla)
print("daniel" in mitupla) #verifica si es verdad o no que el elemento esta en la tupla
#para contar cuantas veces hay un elemento en una tupla
print(mitupla.count("daniel"))
#para imprimir cuantos elementos tiene la tupla
print(len(mitupla))