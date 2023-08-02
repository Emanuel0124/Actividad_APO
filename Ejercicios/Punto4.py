def par_o_impar():
    numero=float(input("Ingrese el numero que desea determinar si es par o impar: "))

    resultado=numero%2
    
    if resultado==0:
        mensaje_par=f"El numero {numero} es par"
        print (mensaje_par)
    else:
        mensaje_impar=f"El numero {numero} es impar"
        print (mensaje_impar)
        