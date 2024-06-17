def sumatoria_matrices():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    matriz1 = []
    matriz2 = []
    
    print("Ingrese los elementos de la primera matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz1.append(fila)
    
    print("Ingrese los elementos de la segunda matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz2.append(fila)
    
    matriz_resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_resultado.append(fila)
    
    print("La matriz resultante es:")
    for fila in matriz_resultado:
        print(fila)

sumatoria_matrices()
