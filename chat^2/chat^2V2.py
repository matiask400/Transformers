import pyautogui
import pyperclip
import google.generativeai as genai
import time
import keyboard

# -----------------------  Avisos  -------------------------
# El codigo proporcionado utiliza la libreria pyautogui para 
# interactuar con la interfaz grafica de usuario
# Utiliza pyperclip para copiar y pegar texto de la papelera
# Escribe la respuesta de GPT en la interfaz de chat utilizando pyautogui
# keyboard en la pestaña que este activa en el momento de la ejecucion
# ----------------------------------------------------------


# Configurar la API de generativeai
genai.configure(api_key="AIzaSyDq1VehLJ3MKEvQFuW8VxmsJ82j2zhbOrw")

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
        time.sleep(30) # Ajustar de ser necesario -----------------------------------
        pyautogui.hotkey("ctrl", "shift", "c")

    def main_loop(self):
        start_time = time.time()
        max_duration = 600  # 10 minutos
        while not self.interrupted and time.time() - start_time < max_duration:
            if self.is_on_chat_page():
                response = self.send_message_gemini()
                self.send_message_gpt(response)
                time.sleep(5)
            else:
                print("No se encontró la página de chat. Esperando...")
                time.sleep(5)

    def is_on_chat_page(self):
        # Captura de pantalla del elemento distintivo
        element_location = pyautogui.locateOnScreen('chat_page_identifier.png', confidence=0.8)
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
