#Programa para recordar listas
#milista = ["daniel", "daniel2", "daniel3", "daniel4"]
#acceder a la posicion 3: milista[3], se guarda daniel3 y asi sucesivamente
import os          #limpiar
os.system('cls')   #limpiar

milista = ["daniel", "daniel2", "daniel3", "daniel4"]
print(milista[0]) #imprimir el elemento
print(milista[0:2]) #imprimir desde este elemento 0 HASTA el otro elemento 2
print(milista[1:]) #imprimir desde este elemento 1 HASTA el final


#para agregar algo AL FINAL de una lista se usa el comando "append"
milista.append("daniel_Mosho")
print(milista[:]) #con ":" se imprime toda la lista

#para insertar algo en la lista se usa el comando "insert"
milista.insert(2,"deniel_Mosho1") #se debe indicar el indica donde se agrega lo que se va a insertar
print(milista[:]) #con ":" se imprime toda la lista

#para insertar una lista seguida a la ya creada se usa el comando "extend"
milista.extend(["daniela", "danielb", "daniec", "danield"]) #se debe indicar el indica donde se agrega lo que se va a insertar
print(milista[:]) #con ":" se imprime toda la lista

#devolver el indice donde esta un elemento
print(milista.index("daniel_Mosho"))

#imprimir falso o verdadero si un elemento esta en la lista
print("daniel_Mosho" in milista)
print("daniel_" in milista)

#remover uel ULTIMO elemento de la lista
milista.pop()
print(milista[:]) #con ":" se imprime toda la lista

#remover un elemento de la lista
milista.remove("daniel4")
print(milista[:]) #con ":" se imprime toda la lista

#unir o sumar dos listas
milista2 = ["0", "1", "2", "3"]
milista3 = milista + milista2
print(milista3[:]) #con ":" se imprime toda la lista

#para imprimir varia veces una lista
milista2 = milista2 * 3
print(milista2[:]) #con ":" se imprime toda la lista