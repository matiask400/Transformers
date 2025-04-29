## Resolución de algoritmos utilizando IA generativas

### Overview
This repository contains code and data used to develop the research paper "Resolución de algoritmos utilizando IA generativas" The project implements an automated pipeline to evaluate large language models (LLMs) from Google and OpenAI under various temperature configurations. A set of curated problems is processed, Python code solutions are generated via structured prompts, those solutions are executed under controlled conditions, and the outcomes are analyzed.

### Project Structure
```
project/
├── data/
│   ├── raw/                  # Raw problem data
│   └── processed/            # Preprocessed problem data for evaluation
├── notebooks/
│   └── 01_processing.ipynb   # Primary notebook to run the evaluation pipeline
├── outputs/
│   ├── outputs/
│   │   └── py_files_outputs_v2/   # Generated Python code files from LLM responses
│   └── visualizations/
│       ├── csv/        # results2; files containing execution and evaluation results
|       └── excel/      # results; files containing the summary
├── src/
│   ├── utils.py
│   └── process_data.py
├── .env
├── requirements.txt
└── README.md
```

### Dependencies and Installation
The project is implemented in Python and leverages several libraries and APIs. Below are the key dependencies:

- **Programming Language:** Python 3.13.0
- **Core Libraries:** csv, os, time, subprocess, pathlib  
- **LLM Integration:**  
  - langchain, langchain-google-genai, langchain-openai, langchain_community  
  - openai  
- **Data and Visualization:** pandas, numpy, matplotlib, seaborn
- **Development Environment:** IPython/Jupyter Notebook  

Install the necessary packages using the following commands within a Jupyter Notebook cell:
```css
%pip install --upgrade --quiet langchain pandas numpy matplotlib seaborn jupyter
%pip install --upgrade --quiet langchain-google-genai openai langchain-openai
%pip install --upgrade --quiet langchain_community
```

### Environment Configuration
Create a `.env` file in the root directory with your API keys. For example:
```ini
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```
*Note: Ensure that `.env` is added to `.gitignore` to protect sensitive information.*

### Execution Process
1. **Problem Extraction:**  
   Problems are read from a preprocessed CSV file located in `data/processed/`.

2. **Prompting the LLMs:**  
   Structured prompts are constructed to extract a Python solution and test examples from each problem.

3. **Code Generation and Execution:**  
   The generated Python code is saved to the `outputs/` directory. Each script is executed with a 60-second timeout using a subprocess, and the output is parsed to count test results.

4. **Result Logging:**  
   Execution details, including counts of "True" and "False" outcomes, are logged in CSV files under `outputs/visualizations/`.

### How to Run
- **Open the Notebook:**  
  Navigate to `notebooks/01_processing.ipynb` and open it in Jupyter Notebook.
  
- **Set Up Environment Variables:**  
  Ensure your `.env` file contains the necessary API keys.
  
- **Execute the Pipeline:**  
  Run the notebook cells sequentially to process the problems, generate code via LLMs, execute the code, and log the results.

### Models Evaluated
- **Google Generative AI Models:**
  - Gemini 1.0 Pro
  - Gemini 1.5 Pro
  - Gemini 1.5 Flash

- **OpenAI Models via LangChain:**
  - GPT-3.5-turbo
  - GPT-4o-mini
  - GPT-4o
  - GPT-4-turbo

### Paper Reference
The methods and results documented in this repository underpin the research paper "Resolución de algoritmos utilizando IA generativas" For further details on the methodology and findings, please refer to the publication.