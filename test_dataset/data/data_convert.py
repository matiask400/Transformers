import csv

# Nombre del archivo de entrada y salida
input_filename = "leetcode_problems.csv"
output_filename = "leetcode_problems_data.csv"

# Lista para almacenar los problemas en formato de diccionario
problems = []

# Leer datos del archivo CSV de entrada
with open(input_filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Saltar el encabezado si es necesario
    next(csv_reader)  # Ignora la primera línea si es un encabezado
    
    # Procesar cada fila del archivo CSV
    for fields in csv_reader:
        # Crear un diccionario para este problema
        problem = {
            "ID": fields[0],
            "Description": fields[2],
        }
        
        # Agregar el diccionario del problema a la lista
        problems.append(problem)

# Escribir datos en el archivo CSV de salida
with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=problem.keys())

    # Escribir encabezados
    writer.writeheader()

    # Escribir filas de datos
    for problem in problems:
        writer.writerow(problem)

print(f"Archivo CSV '{output_filename}' generado exitosamente.")
