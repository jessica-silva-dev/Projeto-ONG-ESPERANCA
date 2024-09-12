# Importando a biblioteca
import customtkinter as ctk
from PIL import Image

# Abrir janela
app = ctk.CTk()

# Titulo
app.title("Projeto Esperança")

# Tamanho da tela
app.geometry("800x600")
app.resizable(False, True)

# Aparencia
ctk.set_appearance_mode("light")

# Logo
logo = ctk.CTkImage(Image.open("imagens/logo.png"), size=(500, 350))
logo_label = ctk.CTkLabel(app, image=logo, text="")  
logo_label.place(x=150, y=20)  

# Parte Nome
nomeLabel = ctk.CTkLabel(app, text="Nome:", font=("Georgia", 16))
nomeLabel.place(x=300, y=350)

nomeEntry = ctk.CTkEntry(app, placeholder_text="Usuário")
nomeEntry.place(x=365, y=350)

# Parte Senha
senhaLabel = ctk.CTkLabel(app, text="Senha:", font=("Georgia", 16))
senhaLabel.place(x=300, y=390)

senhaEntry = ctk.CTkEntry(app, placeholder_text="Senha")
senhaEntry.place(x=365, y=390)

# Botão Entrar
botao = ctk.CTkButton(app, text="Entrar", fg_color="orange", text_color="white", hover_color="darkorange")
botao.place(x=365, y=440)

# Mostrar Janela
app.mainloop()
