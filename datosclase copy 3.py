
def estudiantes_edades():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        estudiantes[nombre] = edad
    
    print("\nListado de estudiantes con sus edades:")
    for nombre, edad in estudiantes.items():
        print(f"Estudiante: {nombre}, Edad: {edad}")

estudiantes_edades()
