import flet as ft
import requests


def toask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False},
    )
    return response.json()["response"]


def create_chat_message(text, user_name):
    return ft.Text(f"{user_name}: {text}", size=16)


def main(page: ft.Page):
    page.title = "JoyAI - Chatbox"
    page.theme_mode = ft.ThemeMode.DARK

    chat_history = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    user_input = ft.TextField(label="Digite algo", expand=True)

    def send_message(e):
        if user_input.value:

            user_text = user_input.value

            chat_history.controls.append(create_chat_message(user_text, "Você"))

            user_input.value = ""
            page.update()

            response = toask_ollama(user_text)

            chat_history.controls.append(create_chat_message(response, "JoyIA"))

            page.update()
            user_input.focus()

    send_button = ft.IconButton(icon=ft.Icons.SEND, on_click=send_message)
    input_row = ft.Row([user_input, send_button])

    page.add(chat_history, input_row)


ft.app(target=main)
