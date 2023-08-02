def preguntar_nombre_y_edad ():
    nombre = str(input("Diga su nombre "))
    edad = int(input("Ingrese su edad "))


    notificacion=f"Hola usuario {nombre}, Tienes {edad} años"
    print (notificacion)