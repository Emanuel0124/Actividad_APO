from Ejercicios import Punto1 as Pt1
from Ejercicios import Punto2 as Pt2
from Ejercicios import Punto3 as Pt3
from Ejercicios import Punto4 as Pt4
from Ejercicios import Punto5 as Pt5
from Ejercicios import Punto6 as Pt6
from Ejercicios import Punto7 as Pt7
from Ejercicios import Punto8 as Pt8
from Ejercicios import Punto9 as Pt9
from Ejercicios import Punto10 as Pt10
from Ejercicios import Punto11 as Pt11
from Ejercicios import Punto12 as Pt12
"""from Ejercicios import Punto6 as Pt13
from Ejercicios import Punto7 as Pt14
from Ejercicios import Punto8 as Pt15"""

while True:
    print("Opcion 1: Punto1 ")
    print("Opcion 2: Punto2 ")
    print("Opcion 3: Punto3 ")
    print("Opcion 4: Punto4 ")
    print("Opcion 5: Punto5 ")
    print("Opcion 6: Punto6 ")
    print("Opcion 7: Punto7 ")
    print("Opcion 8: Punto8 ")
    print("Opcion 9: Punto9 ")
    print("Opcion 10: Punto10 ")
    print("Opcion 11: Punto11 ")
    print("Opcion 12: Punto12 ")
    print("Opcion 13: Punto13 ")
    print("Opcion 14: Punto14 ")
    print("Opcion 15: Punto15 ")
    print("Opcion 16: Salir ")
    opcion=int(input("Ingrese la opcion que desea ejecutar: "))
    
    if (opcion==1):
        print(Pt1.preguntar_nombre_y_edad()) 
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==2):
        print(Pt2.Area_circulo())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))

    elif (opcion==3):
        print(Pt3.lista_alea())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==4):
        print(Pt4.par_o_impar())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==5):
        print(Pt5.Pasar_grados())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==6):
        print(Pt6.suma_de_una_lista_dada())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==7):
        print(Pt7.numero_mayor_y_numero_menor_de_lista())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==8):
        print(Pt8.invertir_lista_dada())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==9):
        print(Pt9.matriz_aleatoria())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==10):
        print(Pt10.factorial_de_un_numero())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==11):
        print(Pt11.lista_numeros_pares())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))
    elif (opcion==12):
        print(Pt12())
        opcion=int(input("Ingrese cualquier numero para volver al menú "))

