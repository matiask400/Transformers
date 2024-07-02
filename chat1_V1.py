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

4. Median of Two Sorted Arrays
Hard
Topics
Companies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106



"""
    response_1 = send_message(chat_session_1, message_1)

    print("-- Resupuesta 1: ", response_1.text)

if __name__ == "__main__":
    main()
