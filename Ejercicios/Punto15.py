def Palindormo_texto():
    
    print("TRUE significa que si es Palindormo")
    print("FALSE significa que no es palindromo")

    texto=str(input("Ingrese una cadena de texto para determinar si es palindromo  "))
    
    texto=texto.replace("","") .lower()
    return(texto==texto[::-1])
    