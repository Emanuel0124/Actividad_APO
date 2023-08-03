import random
def suma_de_una_lista_dada():
    
    lista= [random.randint(0, 20) for x in range(5)]
    
    suma = 0
    for numero in lista:
        suma += numero
    print (lista)
    return suma


    
    