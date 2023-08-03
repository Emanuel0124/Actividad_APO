
def invertir_lista_dada():

    lista = [2,4,6,8,10,12,14]
    length = len(lista)
    print ("las lista es: ",lista)
    for i in range(length // 2):
        lista[i], lista[length - i - 1] = lista[length - i - 1], lista[i]

    mensaje=f"La lista al reves sería: {lista}"

    return mensaje