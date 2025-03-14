#Programa para recordar condicionales

import os          #limpiar
os.system('cls')   #limpiar
print("programa para ingreso de notas de estudiantes")

notalumno = input("Digite la nota del estudiante: ")
#Type (notalumno)

def evaluacion (nota):
    print (nota)
    
    if  nota < 0:
        print("numero invalido")
    elif  nota > 5:
        print("numero invalido")
    elif nota >= 3.0:
        print("Estudiante aprobado")
    elif nota < 3.0:
        print("Estudiante No aprobo")

evaluacion(float (notalumno))
