

def promedio_notas_con_cantidad():
    cantidad = int(input("Ingrese la cantidad de notas: "))
    notas = []
    for _ in range(cantidad):
        nota = float(input("Ingrese una nota: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")

promedio_notas_con_cantidad()
