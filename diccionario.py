#Programa para recordar diccionario

import os          #limpiar
os.system('cls')   #limpiar

midiccionario = {"Lima":"Peru", "Bogota":"Colombia", "BuenosAires":"Argentina"}
print(midiccionario)
#ingresar informacion al diccionario
midiccionario["Madrid"] = "España" 
print(midiccionario)
#reescribir
midiccionario["Madrid"] = "España-Españita" 
print(midiccionario)
#borrar
del midiccionario["Bogota"]
print(midiccionario)