import random
def numero_mayor_y_numero_menor_de_lista():
    lista= [random.randint(0, 50) for x in range(10)]
    maximo = max(lista)
    minimo = min(lista)
    
    mensaje=f"El numero menor de la lista {lista} es: {minimo}  y el mayor es: {maximo}"
    
    
    return mensaje