
def factorial_de_un_numero():
    numero=int(input("Ingrese el numero que desea sacarle el factorial: "))
    acumulador=1
    for i in range(1,numero+1):
        acumulador*=i
    mensaje=f"El factorial de {numero} es: {acumulador}"
    return mensaje