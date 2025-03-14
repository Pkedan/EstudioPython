#ejercicio de sintaxis de funciones

import os          #limpiar
os.system('cls')   #limpiar

def sum (num1, num2):
    print(num1+num2)

def res (num1, num2):
    resultado = num1 - num2
    return resultado

sum (5,5)
sum (5,0)
sum (5,25)
print(res (5, 5))
print(res (5, 0))
print(res (5, 25))