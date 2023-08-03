from Ejercicios import Punto1 as Pt1
from Ejercicios import Punto2 as Pt2
from Ejercicios import Punto3 as Pt3
from Ejercicios import Punto4 as Pt4
from Ejercicios import Punto5 as Pt5
from Ejercicios import Punto6 as Pt6
from Ejercicios import Punto7 as Pt7
"""from Ejercicios import Punto8 as Pt8"""

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


