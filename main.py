import flet as ft


def create_chat_message(text, user_name):
    return ft.Text(f"{user_name}: {text}", size=16)


def main(page: ft.Page):
    page.title = "JoyAI - Chatbox"
    chat_history = ft.Column(scroll=ft.ScrollMode.AUTO)
    page.theme_mode = ft.ThemeMode.DARK

    user_input = ft.TextField(
        label="Olá, eu sou a   JoyAI. Por onde vamos começar hoje?"
    )

    def send_message(e):
        if user_input.value != "":
            new_message = create_chat_message(user_input.value, "você")
            chat_history.controls.append(new_message)

        user_input.value = ""
        user_input.focus()
        page.update()

    send_button = ft.ElevatedButton("Enviar", icon=ft.Icons.SEND, on_click=send_message)
    input_row = ft.Row([user_input, send_button])

    page.add(chat_history, input_row)


# Comando que inicia o app
ft.app(target=main)
