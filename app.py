# Importando a biblioteca
import tkinter as tk
import customtkinter as ctk
from PIL import Image

# Função para criar um gradiente laranja para branco
def criarGradiente(canvas, width, height, iniciarCor, fimCor):
    r1, g1, b1 = canvas.winfo_rgb(iniciarCor)  # Laranja inicial
    r2, g2, b2 = canvas.winfo_rgb(fimCor)    # Branco final
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        cor = f'#{nr:04x}{ng:04x}{nb:04x}'  # Gerando a cor intermediária
        canvas.create_line(0, i, width, i, fill=cor)

# Função para abrir a 2° tela e fechar a 1° já com as configurações iniciais
def segundaTela():
    app.destroy()  
    
    # Criando a segunda janela
    segundaJanela = ctk.CTk()
    segundaJanela.title("Projeto Esperança")
    segundaJanela.geometry("800x600")
    segundaJanela.resizable(False, False)
    ctk.set_appearance_mode("light")
    
    # Menu na lateral 
    menuFrame = ctk.CTkFrame(segundaJanela, width=200, height=600, corner_radius=0)
    menuFrame.place(x=0, y=170)
    menuFrame.configure(bg_color=("orange", "white"))
    
    # Canvas para o gradiente no menu
    canvas = tk.Canvas(menuFrame, width=200, height=600, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    # Gradiente laranja para branco no frame
    criarGradiente(canvas, 200, 600, "#FFA500", "white")
    
    # Label menu inicial
    menuLabel = ctk.CTkLabel(menuFrame, text="Menu inicial", font=("Georgia", 16), fg_color=("orange", "white"), text_color="white")
    menuLabel.place(x=30, y=20)
    
    # Menu cadastro
    cadastroLabel = ctk.CTkLabel(menuFrame, text="Cadastrar", font=("Georgia", 16),fg_color=("orange", "white"), text_color="white")
    cadastroLabel.place(x=40, y=60)
    cadastroLabel.bind("<Button-1>", lambda e: janelaCadastro())
    
    # Menu editar
    editarLabel = ctk.CTkLabel(menuFrame, text="Editar", font=("Georgia", 16),fg_color=("orange", "white"), text_color="white")
    editarLabel.place(x=50, y=100)

    # Imagem das crianças na parte cima 
    imagemCrianca = ctk.CTkImage(Image.open("criancas.png"), size=(800, 150))
    imagemCriancalabel = ctk.CTkLabel(segundaJanela, image=imagemCrianca, text="")  
    imagemCriancalabel.place(x=10, y=10) 
    
    # Parte Nome
    nomeLabel = ctk.CTkLabel(segundaJanela, text="Projeto Esperança", font=("Century Gothic bold", 38))
    nomeLabel.place(x=300, y=170)
    
    # Entry Buscar
    nomeEntryCrianca = ctk.CTkEntry(segundaJanela, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
    nomeEntryCrianca.place(x=330, y=230)

    # Botão buscar
    botaoBuscar = ctk.CTkButton(segundaJanela, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoBuscar.place(x=530, y=230)

    
    def janelaCadastro():
        cadastroCrianca = ctk.CTk()
        cadastroCrianca.title("Cadastro")
        cadastroCrianca.geometry("600x400")
        cadastroCrianca.resizable(False, False)
        ctk.set_appearance_mode("light")
        
        # Titulo
        frameTitulo = ctk.CTkFrame(cadastroCrianca, width=1200, height=30, bg_color="orange", fg_color="orange", corner_radius=0 )
        frameTitulo.place(x=0, y=20)
        texto_frame_titulo = ctk.CTkLabel(frameTitulo, text="Cadastro das Crianças", font=("Century Gothic bold", 18), text_color="white")
        texto_frame_titulo.place(x=195, y=4)
        
        
         # Nome
        nomeLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Nome Completo: ", font=("Georgia", 12))
        nomeLabelCrianca.place(x=20, y=60)
        
        # Entry Nome
        nomeEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Nome da criança", font=("Georgia", 12), width=260)
        nomeEntryCrianca.place(x=115, y=60)
                
        # Idade
        idadeLabelCrianca =  ctk.CTkLabel(cadastroCrianca, text="Idade: ", font=("Georgia", 12))
        idadeLabelCrianca.place(x=395, y=60) 
        opcoesIdade = [str(i) for i in range(13)]
        idadeComboboxCrianca = ctk.CTkComboBox(cadastroCrianca, values= opcoesIdade, font=("Georgia", 12))
        idadeComboboxCrianca.place(x=435, y=60)
        
        # Responsável
        responsavelLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Nome do responsável: ", font=("Georgia", 14))
        responsavelLabelCrianca.place(x=20, y=100)
        
        # Entry responsável
        responsavelEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir nome", font=("Georgia", 14), width=240)
        responsavelEntryCrianca.place(x=170, y=100)
        
        # Endereço
        enderecoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Endereço: ", font=("Georgia", 14))
        enderecoLabelCrianca.place(x=20, y=140)
        
        # Entry endereço
        enderecoEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir endereço", font=("Georgia", 14),width=240)
        enderecoEntryCrianca.place(x=90, y=140)
        
        # Genero
        generoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Sexo: ", font=("Georgia", 14))
        generoLabelCrianca.place(x=20, y=180)
        
        # Vai ser guardado o estado da caixa de seleção na variavel
        masculinoVar = tk.BooleanVar()
        femininoVar = tk.BooleanVar()

        # Sexo
        masculinoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Masculino", 
        variable=masculinoVar,
        onvalue=True, 
        offvalue=False,
        command=lambda: print(f"Masculino selecionado: {masculinoVar.get()}"),
        font=("Georgia", 12) )
        masculinoCheckCrianca.place(x=65, y=180)
        
        # Sexo feminino
        femininoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Feminino", 
        variable=femininoVar,
        onvalue=True, 
        offvalue=False,
        command=lambda: print(f"Feminino selecionado: {femininoVar.get()}"),
        font=("Georgia", 12) )
        femininoCheckCrianca.place(x=160, y=180)
        
        # Contato
        telefoneLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Contato: ", font=("Georgia", 14))
        telefoneLabelCrianca.place(x=270, y=180)
        
        # Entry Contato
        telefoneEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="DDD 000000000", font=("Georgia", 14))
        telefoneEntryCrianca.place(x=330, y=180)
        
        # Tamanho Roupa
        
        # Tamanho Sapato
        
           
        # Botão Salvar
        botaoSalvar = ctk.CTkButton(cadastroCrianca, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoSalvar.place(x=500, y=330)
        
        cadastroCrianca.mainloop()
    
    # Mostrar a segunda janela
    segundaJanela.mainloop()
    
# Função para verificar login
def verificarLogin(event= None):
    usuario = nomeEntry.get()
    senha = senhaEntry.get()
    # Verificação simples do usuário e senha
    if usuario == "1234" and senha == "1234":
        segundaTela()
    else:
        loginErroLabel.configure(text="Usuário ou senha inválidos!")

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
logo = ctk.CTkImage(Image.open("logo.png"), size=(500, 350))
logo_label = ctk.CTkLabel(app, image=logo, text="")  
logo_label.place(x=150, y=20)  

# Parte Nome
nomeLabel = ctk.CTkLabel(app, text="Usuário:", font=("Georgia", 16))
nomeLabel.place(x=300, y=350)

nomeEntry = ctk.CTkEntry(app, placeholder_text="Usuário")
nomeEntry.place(x=365, y=350)

# Parte Senha
senhaLabel = ctk.CTkLabel(app, text="Senha:", font=("Georgia", 16))
senhaLabel.place(x=300, y=390)

senhaEntry = ctk.CTkEntry(app, placeholder_text="Senha", show="*") 
senhaEntry.place(x=365, y=390)

# Label de erro
loginErroLabel = ctk.CTkLabel(app, text="", text_color="red", font=("Georgia", 12))
loginErroLabel.place(x=330, y=425)

# Botão Entrar
botao = ctk.CTkButton(app, text="Entrar", fg_color="orange", text_color="white", hover_color="darkorange", command=verificarLogin)
botao.place(x=365, y=460)

# Usar a tecla "Enter" como botão de login
app.bind('<Return>', verificarLogin)

# Mostrar a janela de login
app.mainloop()