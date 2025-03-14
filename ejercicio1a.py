#ejercicio multiproposito

ex = 0

def limpiar():
    import os          #limpiar
    os.system('cls')   #limpiar

def menu():
    print ("Programa de ayuda matematica")
    print ("")
    print ("Digita 1 Sumar")
    print ("Digita 2 Restar")
    print ("Digita 3 Multiplicar")
    print ("Digita 4 Dividir")
    print ("")   
    print ("Digita 5 Resolver ecuacion cuadratica")
    print ("")    

def SRM():

    print ("Ha seleccionado una opcion: ", opc)
    limpiar()

    a = float (input("Digita un numero: "))
    b = float (input("Digita otro numero: "))
    
    if opc == 1:
        r = a + b
    elif opc == 2:
        r = a - b
    elif opc == 3:
        r = a * b
    elif opc == 4:
        try:
            r = a / b
        except ZeroDivisionError:
             print ("ERROR: La Division Entre Cero no esta definida")
        
    print ("El Resultado: ", r)

while ex != 1:
    limpiar()
    menu ()
    opc = int (input("Digita una opcion: "))

    
    if opc <= 4:
        SRM()
    
    elif opc == 5:
        limpiar()
        print ("Ha seleccionado una opcion 5: ")
        a = float (input("Digita un numero A: "))
        b = float (input("Digita otro numero B: "))
        c = float (input("Digita otro numero C: "))
        try:
            temp = (b*b) - (4*a*c)
            x = (- b + pow (temp,1/2)) / (2*a)
            x2 = (- b - pow (temp,1/2)) / (2*a)
            print ("Resultado X1: ", x)
            print ("Resultado X2: ", x2)
        except ZeroDivisionError:
            print ("ERROR: La Ecuacion estaria divida Entre Cero y no esta definida")
    else:
        print ("")
        print ("En desarrollo")

    print ("")
    ex = int (input ("Digite 1. si desea salir del programa"))