import tkinter as tk
import customtkinter as ctk
from PIL import Image
from db import *

def salvarCriancas():
    nome = nomeEntryCrianca.get()
    responsavel = responsavelEntryCrianca.get()
    idade = idadeComboboxCrianca.get()
    endereco = enderecoEntryCrianca.get()
    contato = telefoneEntryCrianca.get()
    genero = 'Masculino' if masculinoVar.get() else 'Feminino'
    
    conexao = conectarDb()
    if conexao is not None:
        adicionarCriancas(conexao, nome, responsavel, idade, endereco, contato, genero)
        desconectarDb(conexao)

# janela de login
app = ctk.CTk()

# Configurações da janela
app.title("Projeto Esperança")
app.geometry("800x600")
app.resizable(False, False)
ctk.set_appearance_mode("light")

# Logo
logo = ctk.CTkImage(Image.open("logo.png"), size=(500, 350))
logo_label = ctk.CTkLabel(app, image=logo, text="")  
logo_label.place(x=150, y=20)  

# Nome
nomeLabel = ctk.CTkLabel(app, text="Usuário:", font=("Georgia", 16))
nomeLabel.place(x=300, y=350)
nomeEntry = ctk.CTkEntry(app, placeholder_text="Usuário")
nomeEntry.place(x=365, y=350)

# Senha
senhaLabel = ctk.CTkLabel(app, text="Senha:", font=("Georgia", 16))
senhaLabel.place(x=300, y=390)
senhaEntry = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
senhaEntry.place(x=365, y=390)

# Mensagem de senha ou usuario incorreto
loginErroLabel = ctk.CTkLabel(app, text="", text_color="red", font=("Georgia", 12))
loginErroLabel.place(x=360, y=425)

# Função para verificar login
def verificarLogin(event= None):
    usuario = nomeEntry.get()
    senha = senhaEntry.get()
   
    # Verificação simples do usuário e senha
    if usuario == "" and senha == "":
        segundaJanela()
    else:
        loginErroLabel.configure(text="Usuário ou senha inválido!")

# Botão Entrar
botao = ctk.CTkButton(app, text="Entrar", fg_color="orange", text_color="white", hover_color="darkorange", command=verificarLogin)
botao.place(x=365, y=460)
app.bind('<Return>', verificarLogin)

# Janela com os dados das crianças
def segundaJanela():
    app.destroy()  
    # Configurações da janela
    global dadosCriancas
    dadosCriancas = ctk.CTk()
    dadosCriancas.title("Dados das Crianças")
    dadosCriancas.geometry("900x700")
    dadosCriancas.resizable(False, False)
    ctk.set_appearance_mode("light")
   
    # Função para criar o gradiente laranja para branco
    def criarGradiente(canvas, width, height, iniciarCor, fimCor):
        r1, g1, b1 = canvas.winfo_rgb(iniciarCor) 
        r2, g2, b2 = canvas.winfo_rgb(fimCor)  
        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            cor = f'#{nr:04x}{ng:04x}{nb:04x}'
            canvas.create_line(0, i, width, i, fill=cor)
            
    # Frame menu lateral crianças
    menuFrame = ctk.CTkFrame(dadosCriancas, width=80, height=900, corner_radius=0)
    menuFrame.place(x=0, y=120)
    menuFrame.configure(bg_color=("orange", "#FFE5B4"))
    
    # Canvas gradiente menu lateral crianças
    canvas = tk.Canvas(menuFrame, width=80, height=900, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    # Gradiente menu lateral crianças
    criarGradiente(canvas, 80, 900, "#FFA500", "#FFE5B4")
    
    # Canvas gradiente parte superior crianças
    canvasSuperior = tk.Canvas(dadosCriancas, width=1200, height=190, highlightthickness=0)
    canvasSuperior.place(x=0, y=0)
    
    # Gradiente parte superior crianças
    criarGradiente(canvasSuperior, 1200, 190, "#FFE5B4", "#FFA500")
    
    # Imagem das crianças na parte cima crianças
    imagemCrianca = ctk.CTkImage(Image.open("criancas.png"), size=(880, 130))
    imagemCriancalabel = ctk.CTkLabel(dadosCriancas, image=imagemCrianca, text="")  
    imagemCriancalabel.place(x=10, y=10)
    
    # Titulo Projeto Esperança crianças
    nomeLabel = ctk.CTkLabel(dadosCriancas, text="Projeto Esperança", font=("Century Gothic bold", 38))
    nomeLabel.place(x=300, y=160)
    
    # Entry Buscar crianças
    nomeEntryCrianca = ctk.CTkEntry(dadosCriancas, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
    nomeEntryCrianca.place(x=317, y=215)
   
    # Botão buscar crianças
    botaoBuscar = ctk.CTkButton(dadosCriancas, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoBuscar.place(x=533, y=215)
    
    # Botão excluir crianças
    botaoExcluir = ctk.CTkButton(dadosCriancas, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoExcluir.place(x=565, y=660)
   
    # Botão Editar crianças
    botaoEditar = ctk.CTkButton(dadosCriancas, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoEditar.place(x=405, y=660)
   
    # Botão atualizar crianças
    botaoAtualizar = ctk.CTkButton(dadosCriancas, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoAtualizar.place(x=485, y=660)
    
    # Botão Cadastrar crianças
    botaoCadastro = ctk.CTkButton(dadosCriancas, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoCadastro.place(x=315, y=660)
    botaoCadastro.bind("<Button-1>", lambda e: janelaCadastro())
    
    # Jamela de cadastro de mais crianças, ao clicar no botão cadastrar vai abrir essa tela
    def janelaCadastro():
        # Configurações da janela
        global cadastroCrianca, nomeEntryCrianca, responsavelEntryCrianca, idadeComboboxCrianca, enderecoEntryCrianca, telefoneEntryCrianca, masculinoVar, femininoVar
        cadastroCrianca = ctk.CTk()
        cadastroCrianca.title("Cadastro das crianças")
        cadastroCrianca.geometry("600x400")
        cadastroCrianca.resizable(False, False)
        ctk.set_appearance_mode("light")
        cadastroCrianca.grab_set()
       
        # Barra laranja que contem o titulo cdastro das crianças
        frameTitulo = ctk.CTkFrame(cadastroCrianca, width=1200, height=30, bg_color="orange", fg_color="orange", corner_radius=0 )
        frameTitulo.place(x=0, y=20)
        texto_frame_titulo = ctk.CTkLabel(frameTitulo, text="Cadastro das Crianças", font=("Century Gothic bold", 18), text_color="white")
        texto_frame_titulo.place(x=195, y=4)
       
        # Nome cadastro criança
        nomeLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Nome Completo: ", font=("Georgia", 12))
        nomeLabelCrianca.place(x=20, y=80)
        nomeEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Nome da criança", font=("Georgia", 12), width=240)
        nomeEntryCrianca.place(x=170, y=80)
       
        # Idade cadastro criança
        idadeLabelCrianca =  ctk.CTkLabel(cadastroCrianca, text="Idade: ", font=("Georgia", 12))
        idadeLabelCrianca.place(x=305, y=260)
        opcoesIdade = [str(i) for i in range(13)]
        idadeComboboxCrianca = ctk.CTkComboBox(cadastroCrianca, values= opcoesIdade, font=("Georgia", 12))
        idadeComboboxCrianca.place(x=350, y=260)
       
        # Responsável cadastro criança
        responsavelLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Nome do responsável: ", font=("Georgia", 12))
        responsavelLabelCrianca.place(x=20, y=140)
        responsavelEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir nome", font=("Georgia", 12), width=240)
        responsavelEntryCrianca.place(x=170, y=140)
       
        # Endereço cadastro criança
        enderecoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Endereço: ", font=("Georgia", 12))
        enderecoLabelCrianca.place(x=20, y=200)
        enderecoEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="Inserir endereço", font=("Georgia", 12),width=240)
        enderecoEntryCrianca.place(x=170, y=200)
       
        # Genero cadastro criança
        generoLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Sexo: ", font=("Georgia", 16))
        generoLabelCrianca.place(x=185, y=320)
       
        # Sexo masculino cadastro criança
        masculinoVar = tk.BooleanVar()
        masculinoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Masculino",
        variable=masculinoVar,
        onvalue=True,
        offvalue=False,
        font=("Georgia", 12) )
        masculinoCheckCrianca.place(x=230, y=320)
       
        # Sexo feminino cadastro criança
        femininoVar = tk.BooleanVar()
        femininoCheckCrianca = ctk.CTkCheckBox(cadastroCrianca, text="Feminino",
        variable=femininoVar,
        onvalue=True,
        offvalue=False,
        font=("Georgia", 12) )
        femininoCheckCrianca.place(x=325, y=320)
       
        # Contato cadastro criança 
        telefoneLabelCrianca = ctk.CTkLabel(cadastroCrianca, text="Contato: ", font=("Georgia", 12))
        telefoneLabelCrianca.place(x=65, y=260)
        telefoneEntryCrianca = ctk.CTkEntry(cadastroCrianca, placeholder_text="DDD 000000000", font=("Georgia", 12))
        telefoneEntryCrianca.place(x=130, y=260)
       
        # Botão Salvar cadastro criança
        botaoSalvar = ctk.CTkButton(cadastroCrianca, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command=salvarCriancas)
        botaoSalvar.place(x=500, y=330)
       
        cadastroCrianca.mainloop()
    
     # Minimiza a terceira janela quando clicar para abrir a segunda janela
    def minimizarTerceiraJanela():
        if 'dadosPadrinhos' in globals() and    dadosPadrinhos.winfo_exists():
            dadosPadrinhos.iconify() 
        dadosCriancas.deiconify() 
    
    # Icone Criança do menu lateral
    iconeCrianca = ctk.CTkImage(Image.open("icocrianca32.ico"), size=(30, 30))
    iconeCriancaLabel = ctk.CTkLabel(menuFrame, image=iconeCrianca, text="", bg_color=("#FFA500"))
    iconeCriancaLabel.place(x=15, y=50)
    
    # Icone padrinho do menu lateral
    iconePadrinho = ctk.CTkImage(Image.open("prancheta32.ico"), size=(30, 30))
    iconePadrinhoLabel = ctk.CTkLabel(menuFrame, image=iconePadrinho, text="", bg_color=("#FFA500"))
    iconePadrinhoLabel.place(x=15, y=100)
    iconePadrinhoLabel.bind("<Button-1>", lambda e: terceiraJanela())
    
    # Janela com os dados dos padrnhos
    def terceiraJanela():
        dadosCriancas.withdraw()
        # Configurações da janela
        global dadosPadrinhos
        dadosPadrinhos = ctk.CTkToplevel()
        dadosPadrinhos.title("Dados dos Padrinhos")
        dadosPadrinhos.geometry("900x700")
        dadosPadrinhos.resizable(False, False)
        ctk.set_appearance_mode("light")
        
        # Frame menu lateral padrinhos
        menuFrame = ctk.CTkFrame(dadosPadrinhos, width=80, height=900, corner_radius=0)
        menuFrame.place(x=0, y=120)
        menuFrame.configure(bg_color=("orange", "#FFE5B4"))
        
        # Canvas gradiente menu lateral padrinhos
        canvas = tk.Canvas(menuFrame, width=80, height=900, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Gradiente menu lateral padrinhos
        criarGradiente(canvas, 80, 900, "#FFA500", "#FFE5B4")
        
        # Canvas gradiente parte superior padrinhos
        canvasSuperior = tk.Canvas(dadosPadrinhos, width=1200, height=190, highlightthickness=0)
        canvasSuperior.place(x=0, y=0)
        
        # Gradiente parte superior padrinhos
        criarGradiente(canvasSuperior, 1200, 190, "#FFE5B4", "#FFA500")
        
        # Imagem dos padrinhos na parte cima 
        imagemPadrinho = ctk.CTkImage(Image.open("padrinhos.png"), size=(880, 130))
        imagemPadrinholabel = ctk.CTkLabel(dadosPadrinhos, image=imagemPadrinho, text="")  
        imagemPadrinholabel.place(x=10, y=10)

        # Titulo Projeto Esperança padrinhos
        nomeLabel = ctk.CTkLabel(dadosPadrinhos, text="Projeto Esperança", font=("Century Gothic bold", 38))
        nomeLabel.place(x=300, y=160)
        
        # Entry Buscar padrinhos
        nomeEntryCrianca = ctk.CTkEntry(dadosPadrinhos, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
        nomeEntryCrianca.place(x=317, y=215)
    
        # Botão buscar padrinhos
        botaoBuscar = ctk.CTkButton(dadosPadrinhos, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoBuscar.place(x=533, y=215)
        
        # Botão excluir padrinhos
        botaoExcluir = ctk.CTkButton(dadosPadrinhos, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoExcluir.place(x=565, y=660)
    
        # Botão Editar padrinhos
        botaoEditar = ctk.CTkButton(dadosPadrinhos, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoEditar.place(x=405, y=660)
    
        # Botão atualizar padrinhos
        botaoAtualizar = ctk.CTkButton(dadosPadrinhos, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoAtualizar.place(x=485, y=660)
        
        # Botão Cadastrar padrinhos
        botaoCadastro = ctk.CTkButton(dadosPadrinhos, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoCadastro.place(x=315, y=660)
        botaoCadastro.bind("<Button-1>", lambda e: cadastroPadrinhos())

        def cadastroPadrinhos():
            # Configurações da janela
            dadoscadastroPadrinho = ctk.CTk()
            dadoscadastroPadrinho.title("Padrinhos")
            dadoscadastroPadrinho.geometry("600x400")
            dadoscadastroPadrinho.resizable(False, False)
            ctk.set_appearance_mode("light")
            dadoscadastroPadrinho.grab_set()
        
            # Barra laranja que contem o titulo cdastro das padrinhos
            frameTitulo = ctk.CTkFrame(dadoscadastroPadrinho, width=1200, height=30, bg_color="orange", fg_color="orange", corner_radius=0)
            frameTitulo.place(x=0, y=20)
            texto_frame_titulo = ctk.CTkLabel(frameTitulo, text="Cadastro de Padrinhos", font=("Century Gothic bold", 18), text_color="white")
            texto_frame_titulo.place(x=195, y=4)

            # Nome do Padrinho
            nomeLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Nome Completo: ", font=("Georgia", 12))
            nomeLabelPadrinho.place(x=20, y=90)
            nomeEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Nome do padrinho", font=("Georgia", 12), width=260)
            nomeEntryPadrinho.place(x=165, y=90)
    
            # Telefone do Padrinho
            telefoneLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Telefone: ", font=("Georgia", 12))
            telefoneLabelPadrinho.place(x=20, y=150)
            telefoneEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="DDD 000000000", font=("Georgia", 12), width=260)
            telefoneEntryPadrinho.place(x=165, y=150)
        
            # Email padrinhos
            emailLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Email: ", font=("Georgia", 12))
            emailLabelPadrinho.place(x=20, y=210)
            emailEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Email do padrinho", font=("Georgia", 12), width=260)
            emailEntryPadrinho.place(x=165, y=210)
        
            # Criança apadrinhada
            criancaLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Criança Apadrinhada: ", font=("Georgia", 12))
            criancaLabelPadrinho.place(x=20, y=270)
            criancaEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Nome da criança", font=("Georgia", 12), width=260)
            criancaEntryPadrinho.place(x=165, y=270)
        
            # Botão Salvar padrinhos 
            botaoSalvar = ctk.CTkButton(dadoscadastroPadrinho, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
            botaoSalvar.place(x=500, y=330)
            
            dadoscadastroPadrinho.mainloop()
        
         
        
        # Icone Criança do menu lateral
        iconeCrianca = ctk.CTkImage(Image.open("icocrianca32.ico"), size=(30, 30))
        iconeCriancaLabel = ctk.CTkLabel(menuFrame, image=iconeCrianca, text="", bg_color=("#FFA500"))
        iconeCriancaLabel.place(x=15, y=50)
        iconeCriancaLabel.bind("<Button-1>", lambda e: minimizarTerceiraJanela())
        
        # Icone padrinho do menu lateral
        iconePadrinho = ctk.CTkImage(Image.open("prancheta32.ico"), size=(30, 30))
        iconePadrinhoLabel = ctk.CTkLabel(menuFrame, image=iconePadrinho, text="", bg_color=("#FFA500"))
        iconePadrinhoLabel.place(x=15, y=100)
   
        dadosPadrinhos.mainloop()
   
# Mostrar a janela de login
    dadosCriancas.mainloop() # 2° janela dados das crianças
app.mainloop() # 1° janela de login