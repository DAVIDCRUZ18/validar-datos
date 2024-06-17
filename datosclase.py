

def promedio_notas():
    notas = []
    while True:
        nota = input("Ingrese una nota (o 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        notas.append(float(nota))
    
    if len(notas) == 0:
        print("No se ingresaron notas.")
    else:
        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {promedio:.2f}")

promedio_notas()
