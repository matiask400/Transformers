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
        generation_config=generation_config
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
    model1 = model1.upper()
    if model1 == "A":
        model1 = model_option1
    elif model1 == "B":
        model1 = model_option2
    
    print()
    temperature1 = float(input("Model 1 temperature: "))
    
    chat_session_1 = start_conversation(model1, temperature=temperature1, system_instruction="")

    print("-"*50)

    message_1 = """
Problem D
Circular DNA
Time limit: 3 seconds
You have an internship with a bioinformatics research group studying DNA. A single strand of DNA
consists of many genes, which fall into different categories called gene types. Gene types are delimited
by specific nucleotide sequences known as gene markers. Each gene type i has a unique start marker si
and a unique end marker ei. After many dirty jobs (growing bacteria, cell extraction, protein engineering,
and so on), your research group can convert DNA into a form consisting of only the gene markers,
removing all the genetic material lying between the markers.
Your research group came up with the interesting hypothesis that gene interpretation depends on whether
the markers of some gene types form properly nested structures. To decide whether markers of gene type
i form a proper nesting in a given sequence of markers w, one needs to consider the subsequence of w
containing only the markers of gene type i (si and ei), leaving none of them out. The following (and
only the following) are considered to be properly nested structures:
• siei
• siN ei, where N is a properly nested structure
• AB, where A and B are properly nested structures
Given your computing background, you were assigned to investigate this property, but there is one
further complication. Your group is studying a specific type of DNA called circular DNA, which is
DNA that forms a closed loop. To study nesting in circular DNA, it is necessary to cut the loop at some
location, which results in a unique sequence of markers (the direction of reading is fixed by molecular
properties). Whether a gene type i forms a proper nesting now also depends on where the circular
DNA is cut. Your task is to find the cutting location that maximizes the number of gene types that form a
properly nested structure. Figure D.1 shows an example corresponding to Sample Input 1. The indicated
cut results in the markers for gene type 1 being properly nested.e1
e1
s1
e2
s1s2
e42
e1
s1 1
2
3
4
56
7
8
9
Figure D.1: Illustration of Sample Input 1 with its optimal cutting location.
Input
The first line of input contains an integer n (1 ≤ n ≤ 106), the length of the DNA. The next line
contains the DNA sequence, that is, n markers. Each marker is a character c followed by an integer i,
where c ∈ {s, e} specifies whether it is a start or an end marker and i (1 ≤ i ≤ 106) is the gene type of
the marker. The given DNA sequence has been obtained from the circular DNA by cutting at an arbitrary
location.
ICPC World Finals 2019 Problem D: Circular DNA 7
Output
Output one line with two integers p and m, where p is the cutting position that maximizes the number
of different gene types that form a proper nesting, and m is this maximum number of gene types. The
DNA is cut just before the pth input marker (for instance, the cut shown in Figure D.1 has p = 3). If
more than one cutting position yields the same maximum value of m, output the smallest p that does so.
Sample Input 1 Sample Output 1
9
e1 e1 s1 e2 s1 s2 e42 e1 s1
3 1
Sample Input 2 Sample Output 2
8
s1 s1 e3 e1 s3 e1 e3 s3
8 2
"""
    response_1 = send_message(chat_session_1, message_1)

    print("-- Resupuesta 1: ", response_1.text)

if __name__ == "__main__":
    main()
