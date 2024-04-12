def line():
    coefA = float(input("Ingrese el coeficiente A:"))
    coefB = float(input("Ingrese el coeficiente B:"))
    coefX1 = float(input("Ingrese el coeficiente X1:"))
    coefX2 = float(input("Ingrese el coeficiente X2:"))


    print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefX2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefA}X + {coefB}")
    print("")
    print("Dados los siguientes puntos:")


    coefY1 = coefA*coefX1+coefB
    coefY2 = coefA*coefX2+coefB


    print(f"\tP1 ({coefX1}, {coefY1})")
    print(f"\tP2 ({coefX2}, {coefY2})")

    print("")

    distanciaX =(coefX2-coefX1)**2
    distanciaY =(coefY2-coefY1)**2
    
    print(f"La distancia entre ellos es: {(distanciaX+distanciaY)**(1/2)}")


