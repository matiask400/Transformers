from langchain.response_schema import ResponseSchema
from langchain.structured_output_parser import StructuredOutputParser

problem_solution_schema = ResponseSchema(name="problem_solution",
                                        description="""Code a solution in python for these problem.
                                        Answer with the solution, if you don't know the solution output NONE.
                                        Make it to ask for input data examples and check if it returns the output.
                                        In case it does, output True; otherwise, output False.""")

input_output_schemas = [
    ResponseSchema(name="input_1", description="Extract and output input 1 example."),
    ResponseSchema(name="output_1", description="Extract and output output 1 example."),
    ResponseSchema(name="input_2", description="Extract and output input 2 example."),
    ResponseSchema(name="output_2", description="Extract and output output 2 example."),
    ResponseSchema(name="input_3", description="Extract and output input 3 example."),
    ResponseSchema(name="output_3", description="Extract and output output 3 example.")
]

response_schemas = [problem_solution_schema] + input_output_schemas
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

solution_template = """\
For the following text, extract the following information:

{inputs_outputs}

Problem solution: {problem_solution}
Format the output as JSON with the following keys:
Problem solution
Input 1
Output 1
Input 2
Output 2
Input 3
Output 3

text: {text}

{format_instructions}
"""

inputs_outputs = "\n".join([f"{schema.name.capitalize()}: {schema.description}" for schema in input_output_schemas])

print(solution_template.format(inputs_outputs=inputs_outputs, problem_solution=problem_solution_schema.description, format_instructions=format_instructions))
