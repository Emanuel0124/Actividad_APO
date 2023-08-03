
def suma_resta_multiplicacion_division():
    numero1=float(input("Ingrese el primer número "))
    numero2=float(input("Ingrese el segundo número "))

    suma=numero1+numero2
    resta=numero1-numero2
    multiplicacion=numero1*numero2
    division=numero1/numero2

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Todas las anteriores")

    elección=int(input("Ingrese el numero de la opcion que desea realizar "))
    
    if elección==1:
        mensaje=f"La suma de {numero1} + {numero2} es igual a: {suma}"
        print (mensaje)
    elif elección==2:
        mensaje=f"La resta de {numero1} - {numero2} es igual a: {resta}"
        print (mensaje)
    elif elección==3:
        mensaje=f"La multiplicacion de {numero1} * {numero2} es igual a: {multiplicacion}"
        print (mensaje)
    elif elección==4:
        mensaje=f"La division de {numero1} / {numero2} es igual a: {division}"
        print (mensaje)
    elif elección==5:
        mensaje=f"{numero1} + {numero2}= {suma},  {numero1} - {numero2}= {resta},  {numero1} * {numero2}= {multiplicacion},  {numero1} / {numero2}= {division}"
        print(mensaje)
    else:
        print("Opcion inválida")