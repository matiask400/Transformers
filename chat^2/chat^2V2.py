import pyautogui
import pyperclip
import google.generativeai as genai
import time
import keyboard
from datetime import datetime

# Configurar la API de generativeai
genai.configure(api_key="")

# Definir la configuración de generación
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

# Crear el modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

class ChatController:
    def __init__(self):
        self.chat_session = model.start_chat(history=[])
        self.interrupted = False

    def stop_execution(self, event):
        if event.name == 'c' and event.event_type == 'down' and keyboard.is_pressed('ctrl'):
            self.interrupted = True

    def get_last_copied_message(self):
        # Obtener el texto copiado en el portapapeles
        return pyperclip.paste()
    
    def send_message_gemini(self, message=None):
        if message is None:
            # Obtener el último mensaje copiado
            message = self.get_last_copied_message()
            if not message:
                message = "Hola" 
        response = self.chat_session.send_message(message)
        return response

    def send_message_gpt(self, response):
        pyautogui.hotkey("shift", "esc")
        message = response.text.replace("\n", "")
        time.sleep(0.5)
        keyboard.write(message)
        time.sleep(5) # Ajustar de ser necesario -----------------------------------
        pyautogui.press("enter")
        # Copiar ultima respuesta
        time.sleep(50) # Ajustar de ser necesario -----------------------------------
        while not self.is_ready():
            time.sleep(5)
        pyautogui.hotkey("ctrl", "shift", "c")
        return message

    def main_loop(self):
        start_time = time.time()
        max_duration = 18000  # 30 minutos
        while not self.interrupted and time.time() - start_time < max_duration:
            if self.is_on_chat_page():
                response = self.send_message_gemini()
                response_message = self.send_message_gpt(response)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("chats/chat_logs.txt", "a") as file:
                    try:
                        file.write(f"{current_time} - Response: {response_message}\n")
                    except:
                        texto = response_message.encode('ascii', 'replace').decode('ascii')
                        file.write(f"{current_time} - Response: {texto}\n")
                    try:
                        file.write(f"{current_time} - Copied Text: {self.get_last_copied_message()}\n")
                    except:
                        texto = self.get_last_copied_message().encode('ascii', 'replace').decode('ascii')
                        file.write(f"{current_time} - Copied Text: {texto}\n")
                time.sleep(5)
            else:
                print("No se encontró la página de chat. Esperando...")
                time.sleep(5)

    def is_on_chat_page(self):
        # Captura de pantalla del elemento distintivo
        element_location = pyautogui.locateOnScreen('chat_page_identifier.png', confidence=0.8)
        return element_location is not None

    def is_ready(self):
        # Captura de pantalla del elemento distintivo
        try:
            element_location = pyautogui.locateOnScreen('ready.png', confidence=0.5)
        except:
            element_location = True
        return element_location is not None

if __name__ == "__main__":
    chat_controller = ChatController()

    # Suscribir la función stop_execution al evento de presión de tecla
    keyboard.on_press_key('c', chat_controller.stop_execution)

    # Esperar 20 segundos para que la pestaña de chat esté activa
    time.sleep(20)

    # Iniciar el bucle principal
    chat_controller.main_loop()

    # Si la ejecución fue interrumpida por el usuario
    if chat_controller.interrupted:
        print("Ejecución interrumpida por el usuario.")
    else:
        print("Ejecución completada.")

    # Detener la suscripción al evento de presión de tecla
    keyboard.unhook_all()
