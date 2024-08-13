import csv
import time
import subprocess
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

for i in [0, 1]:
    for model in range(3):
        # Google
        llm_models = ["gemini-1.0-pro", "gemini-1.5-pro", "gemini-1.5-flash"]
        llm_model = llm_models[model]
        google_api_key = "AIzaSyD8FTlCUtYp-AOwv0uCuRidehUsiIC9cm8"
        temperature = i
        input_filename = "../data/leetcode_problems.csv"
        output_directory = f"output2/temperature-{temperature}/{llm_model}/"
        results_directory = f"results2/temperature-{temperature}/"
        time_limit = 60

        # Ensure output and results directories exist
        Path(output_directory).mkdir(parents=True, exist_ok=True)
        Path(results_directory).mkdir(parents=True, exist_ok=True)

        # Initialize the chat model
        chat = ChatGoogleGenerativeAI(temperature=temperature, google_api_key=google_api_key, model=llm_model)


        response_schemas = [
            ResponseSchema(
                name="problem_solution",
                description="Code a solution in Python for the given problem. "
                            "The solution should handle example inputs and verify if each output matches the expected result. "
                            "Print for each input the value `True` if the output is correct for that input, otherwise `False`. "
                            "Retun the solution as a Python program. "
            ),
            ResponseSchema(
                name="input_1",
                description="Extract the first example input from the problem description. "
                            "Output it formatted as input in a Python program. "
                            "Do not answer if this information is not found."
            ),
            ResponseSchema(
                name="output_1",
                description="Extract the first example output for comparison in a Python program. "
                            "Do not answer if this information is not found."
            ),
            ResponseSchema(
                name="input_2",
                description="Extract the second example input from the problem description. "
                            "Output it formatted as input in a Python program. "
                            "Do not answer if this information is not found."
            ),
            ResponseSchema(
                name="output_2",
                description="Extract the second example output for comparison in a Python program. "
                            "Do not answer if this information is not found."
            ),
            ResponseSchema(
                name="input_3",
                description="Extract the third example input from the problem description. "
                            "Output it formatted as input in a Python program. "
                            "Do not answer if this information is not found."
            ),
            ResponseSchema(
                name="output_3",
                description="Extract the third example output for comparison in a Python program. "
                            "Do not answer if this information is not found."
            ),
        ]

        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        # Define the prompt template
        solution_template = """
        For the following problem description, extract the following information and format it as JSON:
        
        - "Input 1"
        - "Output 1"
        - "Input 2"
        - "Output 2"
        - "Input 3"
        - "Output 3"
        - "Problem Solution"
        
        Text: {text}
        
        {format_instructions}
        """

        prompt = ChatPromptTemplate.from_template(template=solution_template)

        # List to store problems in dictionary format
        problems = []
        # Read data from the input CSV file
        with open(input_filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Skip the header if needed
            next(csv_reader)  # Skip the first line if it's a header

            # Process each row in the CSV file
            for fields in csv_reader:
                # Create a dictionary for this problem
                problem = {
                    "ID": fields[0],
                    "Description": fields[2],
                }

                # Add the problem dictionary to the list
                problems.append(problem)

        # Initialize an empty list to store data
        datos = []
        print("Datos: {}".format(datos))
        # Define the starting lap and the maximum number of problems to solve
        start_lap = 0  # Start from the (startlap + 1) problem
        max_problems = 25  # Maximum number of problems to solve

        # Limit the number of problems to solve
        for lap in range(start_lap, min(len(problems), start_lap + max_problems)):
            try:
                problem_text = problems[lap]["Description"]

                # Format messages for chat prompt
                messages = prompt.format_messages(text=problem_text,
                                                  format_instructions=format_instructions)

                # Chat with the system and get a response
                response = chat(messages)

                # Take the time before working on the response
                time_start = time.time()

                # Parse the response content using `output_parser`
                output_dict = output_parser.parse(response.content)

                # Extract the code snippet from the response
                python_code = output_dict.get("problem_solution")

                # Process the code to omit the first and last lines
                if "python" in python_code:
                    code_lines = python_code.split('\n')[1:-1]
                    python_code = '\n'.join(code_lines)

                # Save the processed code to a .py file
                output_filename = f"{output_directory}output_{lap + 1}.py"
                with open(output_filename, mode='w', newline='', encoding='utf-8') as pyfile:
                    pyfile.write(python_code)

                print(f"Python code saved successfully in {output_filename}.")

                # Execute the script and capture the output
                script_path = output_filename

                try:
                    # Start the subprocess without the timeout
                    proceso = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    # Use communicate with the timeout
                    salida, _ = proceso.communicate(timeout=time_limit)  # Apply the timeout here

                    resultado = salida.decode().strip()

                    # Count occurrences of "True" and "False" in the output
                    ocurrencias_true = resultado.count("True")
                    ocurrencias_false = resultado.count("False")

                    # Append data to the list
                    datos.append({
                        "ID": lap + 1,
                        "code": python_code,
                        "result": resultado,
                        "true_count": ocurrencias_true,
                        "false_count": ocurrencias_false
                    })
                except subprocess.TimeoutExpired:
                    proceso.kill()
                    datos.append({
                        "ID": lap + 1,
                        "code": python_code,
                        "result": "TIMEOUT",
                        "true_count": "TIMEOUT",
                        "false_count": "TIMEOUT"
                    })

                except (
                SyntaxError, IndentationError, TypeError, ValueError, ImportError, AttributeError, KeyError, IndexError) as e:
                    # Handle specific exceptions separately
                    datos.append({
                        "ID": lap + 1,
                        "code": python_code,  # Include the problematic code
                        "result": str(e),
                        "true_count": "ERROR",
                        "false_count": "ERROR"
                    })

                # Take the time after working on the response
                time_end = time.time()
                # Calculate the time elapsed
                time_elapsed = time_end - time_start

            except Exception as e:
                datos.append({
                    "ID": lap + 1,
                    "code": python_code,
                    "result": str(e),
                    "true_count": "ERROR",
                    "false_count": "ERROR"
                })

            # Pause execution for 15 seconds before next iteration
            if lap < start_lap + max_problems - 1:
                try:
                    if time_elapsed < 10:
                        time.sleep(3 - time_elapsed)
                except NameError:
                    time.sleep(10)
        print("Response: {}".format(response))
        print("Message: {}".format(messages))
        print("output_dict: {}".format(output_dict))
        # Write results to a CSV file

        nombre_archivo = f"{results_directory}results_{llm_model}.csv"
        encabezados = ["ID", "code", "result", "true_count", "false_count"]

        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            if archivo_csv.tell() == 0:
                escritor_csv.writeheader()
            escritor_csv.writerows(datos)

        print(f"CSV file '{nombre_archivo}' created successfully.")
