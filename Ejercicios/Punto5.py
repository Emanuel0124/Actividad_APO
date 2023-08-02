def Pasar_grados():
    farenhei=float(input("Ingrese los grados Farenheit que desea convertir a Celsius: "))
    Celsius=(farenhei-32)*5/9
    mensaje=f"{farenhei} grados Farenheit equivalen a {Celsius} grados Celsius"
    print (mensaje)