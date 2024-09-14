# Importando a biblioteca
import customtkinter as ctk
from PIL import Image

# Função para abrir a 2° tela e fechar a 1° já com as configurações iniciais
def segundaTela():
    app.destroy()  
    
    # Criando a segunda janela
    segundaJanela = ctk.CTk()
    segundaJanela.title("Projeto Esperança")
    segundaJanela.geometry("800x600")
    segundaJanela.resizable(False, False)
    ctk.set_appearance_mode("light")
    
    # Criando as abas
    abas = ctk.CTkTabview(segundaJanela, width=800, height=600)
    abas.place(x=10, y=20)
    
    # Adicionando abas "Crianças" e "Padrinhos"
    abas.add("Crianças")
    abas.add("Padrinhos")
    
    # Aba Crianças 
    
    # Nome
    nomeLabelCrianca = ctk.CTkLabel(abas.tab("Crianças"), text="Nome Completo: ", font=("Georgia", 14))
    nomeLabelCrianca.place(x=20, y=25)
    
    # Entry Nome
    nomeEntryCrianca = ctk.CTkEntry(abas.tab("Crianças"), placeholder_text="Nome da criança", font=("Georgia", 14))
    nomeEntryCrianca.place(x=130, y=25)
    
    # Idade
      = ctk.CTkLabel(abas.tab("Crianças"), text="Idade: ", font=("Georgia", 14))
    idadeLabelCrianca.place(x=300, y=25)
    
    # Entry Idade
    idadeEntryCrianca = ctk.CTkEntry(abas.tab("Crianças"), placeholder_text="Inserir idade", font=("Georgia", 14))
    idadeEntryCrianca.place(x=350, y=25)
    
    # Responsável
    responsavelLabelCrianca = ctk.CTkLabel(abas.tab("Crianças"), text="Nome do responsável: ", font=("Georgia", 14))
    responsavelLabelCrianca.place(x=20, y=70)
    
    # Entry responsável
    responsavelEntryCrianca = ctk.CTkEntry(abas.tab("Crianças"), placeholder_text="Inserir nome", font=("Georgia", 14))
    responsavelEntryCrianca.place(x=170, y=70)
    
    # Endereço
    enderecoLabelCrianca = ctk.CTkLabel(abas.tab("Crianças"), text="Endereço: ", font=("Georgia", 14))
    enderecoLabelCrianca.place(x=320, y=70)
    
    # Entry endereço
    enderecoEntryCrianca = ctk.CTkEntry(abas.tab("Crianças"), placeholder_text="Inserir endereço", font=("Georgia", 14))
    enderecoEntryCrianca.place(x=390, y=70)
    
    
    
    # Aba Padrinhos 
    nomeLabelPadrinho = ctk.CTkLabel(abas.tab("Padrinhos"), text="Nome Completo: ", font=("Georgia", 16))
    nomeLabelPadrinho.place(x=20, y=25)
    
    # Entry Nome
    nomeEntryPadrinho = ctk.CTkEntry(abas.tab("Padrinhos"), placeholder_text="Nome do padrinho", font=("Georgia", 16))
    nomeEntryPadrinho.place(x=150, y=25)
    
    # Contato
    telefoneLabelCrianca = ctk.CTkLabel(abas.tab("Padrinhos"), text="Contato: ", font=("Georgia", 14))
    telefoneLabelCrianca.place(x=250, y=25)
    
    # Entry Contato
    telefoneEntryCrianca = ctk.CTkEntry(abas.tab("Padrinhos"), placeholder_text="DDD 00000 0000", font=("Georgia", 14))
    telefoneEntryCrianca.place(x=290, y=25)
    
    # Mostrar a segunda janela
    segundaJanela.mainloop()
    
# Função para verificar login
def verificarLogin():
    usuario = nomeEntry.get()
    senha = senhaEntry.get()
    
    
    # Verificação simples do usuário e senha
    if usuario == "1234" and senha == "1234":
        segundaTela()
    else:
        loginErroLabel.config(text="Login ou senha incorretas!")

# Abrir a janela de login
app = ctk.CTk()

# Titulo
app.title("Projeto Esperança")

# Tamanho da tela
app.geometry("800x600")
app.resizable(False, False)

# Aparência
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

senhaEntry = ctk.CTkEntry(app, placeholder_text="Senha", show="*")  # Senha escondida
senhaEntry.place(x=365, y=390)

# Label de erro
loginErroLabel = ctk.CTkLabel(app, text="", text_color="red", font=("Georgia", 12))
loginErroLabel.place(x=365, y=420)

# Botão Entrar
botao = ctk.CTkButton(app, text="Entrar", fg_color="orange", text_color="white", hover_color="darkorange", command=verificarLogin)
botao.place(x=365, y=440)

# Mostrar a janela de login
app.mainloop()