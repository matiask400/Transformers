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


def get_last_file_number():
    files = os.listdir("chats_gemini-gemini")
    last_number = len(files)
    return last_number


def start_conversation(model_name, history=None, temperature=1, system_instruction=None):
    if history is None:
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

def save_history(temperature1, temperature2, history, file, model1, model2):
    if not os.path.exists(file):  
        history.insert(0, {
            "generation_config": {
                "temperature model 1": temperature1,
                "temperature model 2": temperature2,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            },
            "safety_settings": [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE",},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE",},
                { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE",},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE",},
            ],
            "model_names": [model1, model2]
        })
    with open(file, 'w') as f:
        json.dump(history, f, indent=2)

def load_history(file):
    with open(file, 'r') as f:
        history = json.load(f)
    return history

def main():
    model_option1 = "gemini-1.5-flash"
    model_option2 = "gemini-1.5-pro"
    date_time = datetime.datetime.now().strftime("%Y%m%d")
    history_file = f"chats_gemini-gemini/conversation_history_{date_time}_{get_last_file_number()}.json"

    if os.path.exists(history_file):
        history = load_history(history_file)
    else:
        history = []

    model1 = input(f"Model 1: \nA: ({model_option1}) \nB: ({model_option2})\n -Option: ")
    if model1 == "A":
        model1 = model_option1
    elif model1 == "B":
        model1 = model_option2

    model2 = input(f"Model 2: \nA: ({model_option1}) \nB: ({model_option2})\n -Option: ")
    if model2 == "A":
        model2 = model_option1
    elif model2 == "B":
        model2 = model_option2
    
    print()
    temperature1 = float(input("Model 1 temperature: "))
    temperature2 = float(input("Model 2 temperature: "))
    
    chat_session_1 = start_conversation(model1, history, temperature=temperature1, system_instruction="You are going to chat with another AI model.")
    chat_session_2 = start_conversation(model2, history, temperature=temperature2, system_instruction="You are going to chat with another AI model.")

    for item in history:
        if item["message"] and item["response"]:
            print("Model 1:", item["message"])
            print("Model 2:", item["response"])

    print("-"*50)
    response_2 = None
    while True:
        if response_2 is None:
            message_1 = input("Input for model 1: ")
        else:
            message_1 = response_2.text
        response_1 = send_message(chat_session_1, message_1)
        history.append({"time": str(datetime.datetime.now()), "message": message_1, "response": response_1.text})
        print("Model 1:", response_1.text)

        time.sleep(20)

        message_2 = response_1.text
        response_2 = send_message(chat_session_2, message_2)
        history.append({"time": str(datetime.datetime.now()), "message": message_2, "response": response_2.text})

        save_history(temperature1, temperature2, history, history_file, model1, model2)

        print("Model 2:", response_2.text)

        time.sleep(20)

if __name__ == "__main__":
    main()
