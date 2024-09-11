# Transformers

## Large Language Model Evaluation

## Project Description
This project aims to evaluate the performance of different large language models through a series of standardized tests. Using a Python program executed in IPython, we assess the models' ability to solve problems from "Problem Set 4," experimenting with different temperature settings to observe their impact on the generated results.

## Technologies Used
- **Language**: Python
- **Environment**: IPython
- **Libraries**:
  - `csv`: For handling CSV file operations.
  - `os`: For interacting with the operating system.
  - `time`: For time-related operations.
  - `subprocess`: To run the program under controlled conditions.
  - `openai`: For integration with OpenAI models.
  - `pathlib`: For working with file paths.
  - `langchain_google_genai`: For integration with Google Generative AI models.
  - `langchain.prompts.ChatPromptTemplate`: For creating prompts for the models.
  - `langchain.output_parsers`: For parsing model responses.
  - `langchain.chat_models.ChatOpenAI`: For using OpenAI's chat models.

## Repository
The code is available on GitHub [here](https://github.com/matiask400/Transformers). All necessary documentation is included for easy review.

## Models Used
- **Models**:
  - Gemini 1.0 Pro 
  - Gemini 1.5 Pro
  - Gemini 1.5 Flash
  - GPT 3.5-turbo
  - GPT 4.0-turbo
  - GPT-4o 
  - GPT 4o-mini

## Execution Configuration
- **Temperatures tested**:
  - Temperature = 0
  - Temperature = 1
- **Additional parameters**:
  - `top_p = 1`
- **Prompt**: Solve problems from "Problem Set 4" with the model returning "True" for successful tests and "False" otherwise.

## Execution Process
1. **Problem Selection**: The first 25 problems from "Problem Set 4".
2. **Execution**:
   - The prompt was sent to the models with the indicated configuration.
   - The model's response was extracted from the resulting JSON and stored in a Python file.
   - The Python file was executed using `subprocess` with a 60-second time limit.
3. **Result Analysis**:
   - Counting "True" and "False" responses.
   - Results were stored in a CSV file along with the execution code.

## Main Executable Notebook
The primary notebook responsible for executing the program is located at:
/Transformers/test_dataset/process_data/Solve_Extract_V2.ipynb
To run the program, navigate to the directory and execute the notebook.

## Generated Files
- **Results CSV**: Contains the count of "True" and "False" responses along with execution details.
- **Python Code**: Contains the code used for the evaluation.

## Conclusions
This project offers a detailed comparison of large language models under different temperature configurations, highlighting how these variables affect the models' ability to solve these problems.
