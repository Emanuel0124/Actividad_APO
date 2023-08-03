import random
def media_aritmetica():
    acumulador=0
    contador=0
    numero=int(input("Ingrese el numero de datos que va a contener la lista: "))
    lista=[0]
    for i in range(1,numero+1):
        lista.append(i)
        acumulador+=lista[i]
        contador+=1
    promedio=acumulador/contador
    mensaje=f"el promedio de los numeros de la lista {lista}, es: {promedio}"
    return mensaje

