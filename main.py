import flet as ft

def main (page: ft.Page):
    page.title = "Meu Primeiro App IA - Joyce"
    page.theme_mode = ft.ThemeMode.DARK
 
    # Criando um elemento de texto (O famoso Olá Mundo!)
    user_input = ft.TextField(label= "Olá, eu sou a   JoyAI. Por onde vamos começar hoje?")
    ai_response = ft.Text(value="Aguardando...")

    def send_message (e):
        ai_response.value = user_input.value
        user_input.value = ""    # Adicionando o elemento na tela
        page.update()
    
    send_button = ft.ElevatedButton("Send", on_click=send_message)
    page.add(
        user_input, 
        send_button,
        ai_response       
        )

# Comando que inicia o app
ft.app(target=main)