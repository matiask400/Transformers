import pyautogui
import pyperclip
import google.generativeai as genai
import time
import keyboard
from datetime import datetime
import sys
import os

# Get the current directory (where my_script.py is located)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

# Now you can import GEMINI_API_KEY from archivo.py
from archivo import GEMINI_API_KEY

# Configure the generativeai API
GEMINI_API_KEY = GEMINI_API_KEY()
genai.configure(api_key=GEMINI_API_KEY)

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

def ensure_safe_start():
    option = input("Press Y to start the chat...")
    if option != "Y":
        keyboard.unhook_all()
        print("Chat not initiated.")
        exit()
    pyautogui.alert("The program will run in 20 seconds. Make sure to have the chat tab active.", "Notice", button="Understood")
    print("Starting chat in 20 seconds...")

class ChatController:
    def __init__(self):
        self.chat_session = model.start_chat(history=[])
        self.interrupted = False

    def stop_execution(self, event):
        if event.name == 'c' and event.event_type == 'down' and keyboard.is_pressed('ctrl'):
            self.interrupted = True

    def get_last_copied_message(self):
        # Get the copied text from the clipboard
        return pyperclip.paste()
    
    def send_message_gemini(self, message=None):
        if message is None:
            # Get the last copied message
            message = self.get_last_copied_message()
            if not message:
                message = "Hello" 
        response = self.chat_session.send_message(message)
        return response

    def send_message_gpt(self, response):
        pyautogui.hotkey("shift", "esc")
        message = response.text.replace("\n", "")
        time.sleep(0.5)
        keyboard.write(message)
        time.sleep(5) # Adjust if necessary -----------------------------------
        pyautogui.press("enter")
        # Copy last response
        time.sleep(50) # Adjust if necessary -----------------------------------
        while not self.is_ready():
            time.sleep(5)
        pyautogui.hotkey("ctrl", "shift", "c")
        return message

    def main_loop(self):
        start_time = time.time()
        max_duration = 18000  # 30 minutes
        while not self.interrupted and time.time() - start_time < max_duration:
            if self.is_on_chat_page():
                response = self.send_message_gemini()
                response_message = self.send_message_gpt(response)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("chats/chat_logs.txt", "a") as file:
                    try:
                        file.write(f"{current_time} - Response: {response_message}\n")
                    except:
                        text = response_message.encode('ascii', 'replace').decode('ascii')
                        file.write(f"{current_time} - Response: {text}\n")
                    try:
                        file.write(f"{current_time} - Copied Text: {self.get_last_copied_message()}\n")
                    except:
                        text = self.get_last_copied_message().encode('ascii', 'replace').decode('ascii')
                        file.write(f"{current_time} - Copied Text: {text}\n")
                time.sleep(5)
            else:
                print("Chat page not found. Waiting...")
                time.sleep(5)

    def is_on_chat_page(self):
        # Screenshot of the distinctive element
        element_location = pyautogui.locateOnScreen('images/chat_page_identifier.png', confidence=0.8)
        return element_location is not None

    def is_ready(self):
        # Screenshot of the distinctive element
        try:
            element_location = pyautogui.locateOnScreen('images/ready.png', confidence=0.5)
        except:
            element_location = True
        return element_location is not None

if __name__ == "__main__":
    chat_controller = ChatController()

    # Subscribe the stop_execution function to the key press event
    keyboard.on_press_key('c', chat_controller.stop_execution)

    # Wait 20 seconds for the chat tab to be active
    ensure_safe_start()
    time.sleep(20)

    # Start the main loop
    chat_controller.main_loop()

    # If execution was interrupted by the user
    if chat_controller.interrupted:
        print("Execution interrupted by the user.")
    else:
        print("Execution completed.")

    # Unsubscribe from the key press event
    keyboard.unhook_all()
