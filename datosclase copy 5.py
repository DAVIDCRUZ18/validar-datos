def tabla_multiplicacion():
    n = int(input("Ingrese el tamaño de la tabla de multiplicar: "))
    
    matriz_multiplicacion = [[(i+1)*(j+1) for j in range(n)] for i in range(n)]
    
    print("Tabla de multiplicar:")
    for fila in matriz_multiplicacion:
        print("\t".join(map(str, fila)))

tabla_multiplicacion()
