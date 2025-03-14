#ejercicio multiproposito

ex = 0

def limpiar():
    import os          #limpiar
    os.system('cls')   #limpiar

while ex != 1:
    limpiar()
    print ("Programa de ayuda matematica")
    print ("")
    print ("Digita 1 Sumar")
    print ("Digita 2 Restar")
    print ("Digita 3 Multiplicar")
    print ("Digita 4 Dividir")
    print ("")   
    print ("Digita 5 Resolver ecuacion cuadratica")
    print ("")    
    opc = int (input("Digita una opcion: "))

    if opc == 1:
        limpiar()
        print ("Ha seleccionado una opcion 1: ")
        a = float (input("Digita un numero: "))
        b = float (input("Digita otro numero: "))
        r = a + b
        print ("Resultado: ", r)
    
    elif opc == 2:
        limpiar()
        print ("Ha seleccionado una opcion 2: ")
        a = float (input("Digita un numero: "))
        b = float (input("Digita otro numero: "))
        r = a - b
        print ("Resultado: ", r)

    elif opc == 3:
        limpiar()
        print ("Ha seleccionado una opcion 3: ")
        a = float (input("Digita un numero: "))
        b = float (input("Digita otro numero: "))
        r = a * b
        print ("Resultado: ", r)

    elif opc == 4:
        limpiar()
        print ("Ha seleccionado una opcion 4: ")
        a = float (input("Digita un numero: "))
        b = float (input("Digita otro numero: "))
        if b == 0:
            print ("No definido un numero divido entre Cero")
        else:
            r = a / b
            print ("Resultado: ", r)

    elif opc == 5:
        limpiar()
        print ("Ha seleccionado una opcion 5: ")
        a = float (input("Digita un numero A: "))
        b = float (input("Digita otro numero B: "))
        c = float (input("Digita otro numero C: "))
        temp = (b*b) - (4*a*c)
        x = (- b + pow (temp,1/2)) / (2*a)
        x2 = (- b - pow (temp,1/2)) / (2*a)
        print ("Resultado X1: ", x)
        print ("Resultado X2: ", x2)
    else:
        print ("")
        print ("En desarrollo")

    print ("")
    ex = int (input ("Digite 1. si desea salir del programa"))