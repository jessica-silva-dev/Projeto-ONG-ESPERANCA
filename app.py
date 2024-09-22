#atual
# Importando as bibliotecas necessárias
import tkinter as tk
import customtkinter as ctk
from PIL import Image

# Função para criar o gradiente laranja para branco
def criarGradiente(canvas, width, height, iniciarCor, fimCor):
    r1, g1, b1 = canvas.winfo_rgb(iniciarCor)  # Laranja inicial
    r2, g2, b2 = canvas.winfo_rgb(fimCor)      # Branco final
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        cor = f'#{nr:04x}{ng:04x}{nb:04x}'  # Cor intermediária
        canvas.create_line(0, i, width, i, fill=cor)

# Função para abrir a 3° tela e fechar a 1° já com as configurações iniciais        
def terceiraJanela():
    segundaJanela.destroy()
    
    # Criando a terceira janela
    dadosPadrinhos =ctk.CTk()
    dadosPadrinhos.title("Projeto Esperança")
    dadosPadrinhos.geometry("900x700")
    dadosPadrinhos.resizable(False, False)
    ctk.set_appearance_mode("light")

    # Menu na lateral 
    menuFrame = ctk.CTkFrame(dadosPadrinhos, width=100, height=600, corner_radius=0)
    menuFrame.place(x=0, y=143)
    menuFrame.configure(bg_color=("orange", "#FFE5B4"))
        
    # Canvas para o gradiente no menu lateral  (Conteiner)
    canvas = tk.Canvas(menuFrame, width=70, height=600, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    # Gradiente laranja para branco no frame menu lateral (Gradiente)
    criarGradiente(canvas, 300, 600, "#FFA500", "#FFE5B4")
    
    # Canvas para o gradiente embaixo da imagem (Conteiner superior)
    canvasSuperior = tk.Canvas(dadosPadrinhos, width=900, height=120, highlightthickness=0)
    canvasSuperior.place(x=0, y=0)  
    
    # Criando o gradiente laranja para branco na parte superior (Gradiente)
    criarGradiente(canvasSuperior, 900, 150, "#FFE5B4", "#FFA500")

    # Carregando os ícones
    iconeCrianca = ctk.CTkImage(Image.open("icocrianca24.ico"), size=(30, 30))
    iconePadrinho = ctk.CTkImage(Image.open("prancheta32.ico"), size=(30, 30))

    # Adicionando os ícones ao menu
    #label crianças
    iconeCriancaLabel = ctk.CTkLabel(menuFrame, image=iconeCrianca, text="", bg_color=("#FFA500"))
    iconeCriancaLabel.place(x=10, y=50)

    #label padrinhos
    iconePadrinhoLabel = ctk.CTkLabel(menuFrame, image=iconePadrinho, text="", bg_color=("#FFA500"))
    iconePadrinhoLabel.place(x=10, y=100)
    
    # Imagem das crianças na parte cima 
    imagemCrianca = ctk.CTkImage(Image.open("1.png"), size=(879, 120))
    imagemCriancalabel = ctk.CTkLabel(dadosPadrinhos, image=imagemCrianca, text="")  
    imagemCriancalabel.place(x=10, y=10) 
    
    # Parte Nome
    nomeLabel = ctk.CTkLabel(dadosPadrinhos, text="Projeto Esperança", font=("Century Gothic bold", 35))
    nomeLabel.place(x=300, y=120)
    
    # Entry Buscar
    nomeEntryPadrinho = ctk.CTkEntry(dadosPadrinhos, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
    nomeEntryPadrinho.place(x=317, y=215)
    
    # Botão buscar
    botaoBuscar = ctk.CTkButton(dadosPadrinhos, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoBuscar.place(x=533, y=215)
    
    # Botão Cadastra
    botaoCadastro = ctk.CTkButton(dadosPadrinhos, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoCadastro.place(x=295, y=660)
    botaoCadastro.bind("<Button-1>", lambda e: cadastroPadrinhos())
    
    # Botão excluir
    botaoExcluir = ctk.CTkButton(dadosPadrinhos, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoExcluir.place(x=545, y=660)
    
    # Botão Editar
    botaoEditar = ctk.CTkButton(dadosPadrinhos, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoEditar.place(x=385, y=660)
    
    # Botão atualizar
    botaoAtualizar = ctk.CTkButton(dadosPadrinhos, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoAtualizar.place(x=465, y=660)
    
    def cadastroPadrinhos():
        dadoscadastroPadrinho = ctk.CTk()
        dadoscadastroPadrinho.title("Padrinhos")
        dadoscadastroPadrinho.geometry("600x400")
        dadoscadastroPadrinho.resizable(False, False)
        ctk.set_appearance_mode("light")
        
        # Título
        frameTitulo = ctk.CTkFrame(dadoscadastroPadrinho, width=1200, height=30, bg_color="orange", fg_color="orange", corner_radius=0)
        frameTitulo.place(x=0, y=20)
        texto_frame_titulo = ctk.CTkLabel(frameTitulo, text="Cadastro de Padrinhos", font=("Century Gothic bold", 18), text_color="white")
        texto_frame_titulo.place(x=195, y=4)
        
        # Nome do Padrinho
        nomeLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Nome Completo: ", font=("Georgia", 12))
        nomeLabelPadrinho.place(x=20, y=90)
        
        # Entry Nome Padrinho
        nomeEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Nome do padrinho", font=("Georgia", 12), width=260)
        nomeEntryPadrinho.place(x=165, y=90)
        
        # Telefone do Padrinho
        telefoneLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Telefone: ", font=("Georgia", 12))
        telefoneLabelPadrinho.place(x=20, y=150) 
        telefoneEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="DDD 000000000", font=("Georgia", 12), width=260)
        telefoneEntryPadrinho.place(x=165, y=150)
        
        # Email do Padrinho
        emailLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Email: ", font=("Georgia", 12))
        emailLabelPadrinho.place(x=20, y=210)
        emailEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Email do padrinho", font=("Georgia", 12), width=260)
        emailEntryPadrinho.place(x=165, y=210)
        
        # Criança apadrinhada
        criancaLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Criança Apadrinhada: ", font=("Georgia", 12))
        criancaLabelPadrinho.place(x=20, y=270)
        criancaEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Nome da criança", font=("Georgia", 12), width=260)
        criancaEntryPadrinho.place(x=165, y=270)
        
        # Botão Salvar
        botaoSalvar = ctk.CTkButton(dadoscadastroPadrinho, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoSalvar.place(x=500, y=330)
        
        dadoscadastroPadrinho.mainloop()

# Função para abrir a 2° tela e fechar a 1° já com as configurações iniciais
def segundaJanela():
    app.destroy()  
    
    # Criando a segunda janela
    dadosCriancas = ctk.CTk()
    dadosCriancas.title("Projeto Esperança")
    dadosCriancas.geometry("900x700")
    dadosCriancas.resizable(False, False)
    ctk.set_appearance_mode("light")
    
    # Menu na lateral esquerda
    menuFrame = ctk.CTkFrame(dadosCriancas, width=100, height=600, corner_radius=0)
    menuFrame.place(x=0, y=143)
    menuFrame.configure(bg_color=("orange", "#FFE5B4"))
        
    # Canvas para o gradiente no menu lateral esquerda
    canvas = tk.Canvas(menuFrame, width=50, height=600, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    
    # Carregando os ícones
    iconeCrianca = ctk.CTkImage(Image.open(r"icocrianca32.ico"), size=(30, 30))
    iconePadrinho = ctk.CTkImage(Image.open(r"prancheta32.ico"), size=(30, 30))

    # Adicionando os ícones ao menu
    iconeCriancaLabel = ctk.CTkLabel(menuFrame, image=iconeCrianca, text="", bg_color=("#FFA500"))
    iconeCriancaLabel.place(x=10, y=50)

    iconePadrinhoLabel = ctk.CTkLabel(menuFrame, image=iconePadrinho, text="", bg_color=("#FFA500"))
    iconePadrinhoLabel.place(x=10, y=100)

    # Gradiente laranja para branco no frame lateral esqueda
    criarGradiente(canvas, 300, 600, "#FFA500", "#FFE5B4")
    
    # Canvas para o gradiente logo abaixo da imagem
    canvasSuperior = tk.Canvas(dadosCriancas, width=900, height=150, highlightthickness=0)
    canvasSuperior.place(x=0, y=0)  # Posicionado abaixo da imagem

    # Criando o gradiente laranja para branco na parte superior
    criarGradiente(canvasSuperior, 900, 150, "#FFE5B4", "#FFA500")

    # Imagem das crianças na parte cima 
    imagemCrianca = ctk.CTkImage(Image.open("White Minimalist Simple Aesthetic Name Twitter Header.png"), size=(880, 130))
    imagemCriancalabel = ctk.CTkLabel(dadosCriancas, image=imagemCrianca, text="")  
    imagemCriancalabel.place(x=10, y=10) 
    
    # Parte Nome
    nomeLabel = ctk.CTkLabel(dadosCriancas, text="Projeto Esperança", font=("Century Gothic bold", 38))
    nomeLabel.place(x=300, y=160)
    
    # Entry Buscar
    nomeEntryCrianca = ctk.CTkEntry(dadosCriancas, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
    nomeEntryCrianca.place(x=317, y=215)
    
    # Botão buscar
    botaoBuscar = ctk.CTkButton(dadosCriancas, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoBuscar.place(x=533, y=215)
    
    # Botão Cadastra
    botaoCadastro = ctk.CTkButton(dadosCriancas, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoCadastro.place(x=295, y=660)
    botaoCadastro.bind("<Button-1>", lambda e: janelaCadastro())
    
    # Botão excluir
    botaoExcluir = ctk.CTkButton(dadosCriancas, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoExcluir.place(x=545, y=660)
    
    # Botão Editar
    botaoEditar = ctk.CTkButton(dadosCriancas, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoEditar.place(x=385, y=660)
    
    # Botão atualizar
    botaoAtualizar = ctk.CTkButton(dadosCriancas, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoAtualizar.place(x=465, y=660)
    
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
        nomeLabelCrianca.place(x=20, y=80)
        
        # Entry Nome
        nomeEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Nome da criança", font=("Georgia", 12), width=240)
        nomeEntryCrianca.place(x=170, y=80)
        
        # Idade
        idadeLabelCrianca =  ctk.CTkLabel(cadastroCrianca, text="Idade: ", font=("Georgia", 12))
        idadeLabelCrianca.place(x=305, y=260) 
        opcoesIdade = [str(i) for i in range(13)]
        idadeComboboxCrianca = ctk.CTkComboBox(cadastroCrianca, values= opcoesIdade, font=("Georgia", 12))
        idadeComboboxCrianca.place(x=350, y=260)
        
        # Responsável
        responsavelLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Nome do responsável: ", font=("Georgia", 12))
        responsavelLabelCrianca.place(x=20, y=140)
        
        # Entry responsável
        responsavelEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir nome", font=("Georgia", 12), width=240)
        responsavelEntryCrianca.place(x=170, y=140)
        
        # Endereço
        enderecoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Endereço: ", font=("Georgia", 12))
        enderecoLabelCrianca.place(x=20, y=200)
        
        # Entry endereço
        enderecoEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir endereço", font=("Georgia", 12),width=240)
        enderecoEntryCrianca.place(x=170, y=200)
        
        # Genero
        generoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Sexo: ", font=("Georgia", 16))
        generoLabelCrianca.place(x=185, y=320)
        
        # Sexo masculino
        masculinoVar = tk.BooleanVar()
        masculinoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Masculino", 
        variable=masculinoVar,
        onvalue=True, 
        offvalue=False,
        font=("Georgia", 12) )
        masculinoCheckCrianca.place(x=230, y=320)
        
        # Sexo feminino
        femininoVar = tk.BooleanVar()
        femininoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Feminino", 
        variable=femininoVar,
        onvalue=True, 
        offvalue=False,
        font=("Georgia", 12) )
        femininoCheckCrianca.place(x=325, y=320)
        
        # Contato
        telefoneLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Contato: ", font=("Georgia", 12))
        telefoneLabelCrianca.place(x=65, y=260)
        
        # Entry Contato
        telefoneEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="DDD 000000000", font=("Georgia", 12))
        telefoneEntryCrianca.place(x=130, y=260)
        
        # Botão Salvar
        botaoSalvar = ctk.CTkButton(cadastroCrianca, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoSalvar.place(x=500, y=330)
        
        cadastroCrianca.mainloop()
    
    # Mostrar a segunda janela
    dadosCriancas.mainloop()
    
    # Função para verificar login
def verificarLogin(event= None):
    usuario = nomeEntry.get()
    senha = senhaEntry.get()
    
    # Verificação simples do usuário e senha
    if usuario == "" and senha == "":
        segundaJanela()
    else:
        loginErroLabel.configure(text="Usuário ou senha inválido!")

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
loginErroLabel.place(x=360, y=425)

# Botão Entrar
botao = ctk.CTkButton(app, text="Entrar", fg_color="orange", text_color="white", hover_color="darkorange", command=verificarLogin)
botao.place(x=365, y=460)

# Usar a tecla "Enter" como botão de login
app.bind('<Return>', verificarLogin)

# Mostrar a janela de login
app.mainloop()
