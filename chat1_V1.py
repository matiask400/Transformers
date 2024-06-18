import sys
import os
import datetime
import json
import time
import google.generativeai as genai
import google.api_core.exceptions

# Configure the generativeai API
# Get the current directory (where archivo.py is located)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from archivo import GEMINI_API_KEY

GEMINI_API_KEY = GEMINI_API_KEY()


def start_conversation(model_name, temperature=1, system_instruction=None):
    history = []
    genai.configure(api_key=GEMINI_API_KEY)
    generation_config = {
        "temperature": temperature,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE",},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE",},
        { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE",},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE",},
    ]
    model = genai.GenerativeModel(
        model_name=model_name,
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instruction,
    )
    chat_session = model.start_chat(history=history)
    return chat_session

def send_message(chat_session, message):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = chat_session.send_message(message)
            return response
        except google.api_core.exceptions.DeadlineExceeded as e:
            print(f"Error: {e}")
            print(f"Retrying... (Attempt {attempt + 1}/{max_retries}, waiting {2 ** attempt} seconds)")
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                raise e


def main():
    model_option1 = "gemini-1.5-flash"
    model_option2 = "gemini-1.5-pro"

    model1 = input(f"Model 1: \nA: ({model_option1}) \nB: ({model_option2})\n -Option: ")
    if model1 == "A":
        model1 = model_option1
    elif model1 == "B":
        model1 = model_option2
    
    print()
    temperature1 = float(input("Model 1 temperature: "))
    
    chat_session_1 = start_conversation(model1, temperature=temperature1, system_instruction="You are going to solve a algorithm")

    print("-"*50)

    message_1 = """Problema: Ayudando al profe

Un profesor de la UTN tiene que resolver el problema de redondear las notas de sus alumnos. Como tiene muchos alumnos y las reglas son varias entonces decide hacer un programa que lo haga por él. 

Las notas de su materia van del 0 al 100 ambos inclusive
Las notas menores a 40 son notas NO APROBADAS.

Las reglas de redondeo que quiere utilizar este profesor son las siguientes:

Si la diferencia entre la nota actual y el próximo múltiplo de 5 es menor a 3 entonces se redondea al próximo múltiplo de 5.
Si la nota es menor que 38 no hay redondeo ya que el resultado sigue siendo una nota no aprobada. 

Por ejemplo, la nota 84 es redondeada a 85 (próximo múltiplo de 5) pero la nota 29 queda en ese valor.

Entrada:
Se incluyen como entradas:
La primera línea contiene un entero (1< N < 1000) con la cantidad de notas de alumnos que van a ir en la entrada.
Las siguientes líneas contienen las N notas, una nota por cada línea.
Salida
La salida debe consistir en N líneas conteniendo las notas luego del redondeo de acuerdo a las reglas en el mismo orden que entraro"""
    response_1 = send_message(chat_session_1, message_1)

    print("-- Resupuesta 1: ", response_1.text)

if __name__ == "__main__":
    main()
