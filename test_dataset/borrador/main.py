import csv
import google.generativeai as genai

genai.configure(api_key=os.environ["YOUR_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="""
  Devolver en este formato 
      Solución en python del problema: ´´´ ´´´ 
      Input 1 del problema: ´´´ ´´´
      Output 1 del problema: ´´´ ´´´
      Input 2 del problema: ´´´ ´´´
      Output 2 del problema: ´´´ ´´´
      Input 3 del problema: ´´´ ´´´
      Output 3 del problema: ´´´ ´´´
  """,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)

# Nombre del archivo de entrada y salida
input_filename = "leetcode_problems_data.csv"

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
            "Title": fields[1],
            "Description": fields[2],
            "Difficulty": fields[3],
            "Premium": fields[4],
            "Solution Link": fields[5],
            "Acceptance Rate": fields[6],
            "Frequency": fields[7],
            "URL": fields[8],
            "Discuss Count": fields[9],
            "Accepted": fields[10],
            "Submissions": fields[11],
            "Companies": fields[12],
            "Related Topics": fields[13],
            "Likes": fields[14],
            "Dislikes": fields[15],
            "Rating": fields[16],
            "Asked by FAANG": fields[17],
            "Similar Questions": fields[18] if len(fields) > 18 else "",  # Manejar casos donde no hay Similar Questions
        }
        # Agregar un atributo adicional al diccionario del problema
        problem["input_1"] = "Some value"
        problem["output_1"] = "Some value"
        problem["input_2"] = "Some value"
        problem["output_2"] = "Some value"
        problem["input_3"] = "Some value"
        problem["output_3"] = "Some value"
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
