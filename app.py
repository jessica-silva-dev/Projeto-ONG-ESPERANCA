import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from db import *

# Funcionalidades dos botôes
# Função para limpar os campos de cadastro criança 
def limpaCamposCrianca():
    nomeEntryCrianca.delete(0, ctk.END)
    responsavelEntryCrianca.delete(0, ctk.END)
    idadeComboboxCrianca.set('')
    enderecoEntryCrianca.delete(0, ctk.END)
    telefoneEntryCrianca.delete(0, ctk.END)

# Função para limpar os campos de cadastro padrinhos 
def limpaCamposPadrinho():
    nomeEntryPadrinho.delete(0, ctk.END)
    telefoneEntryPadrinho.delete(0, ctk.END)
    emailEntryPadrinho.delete(0, ctk.END)
    enderecoEntryPadrinho.delete(0, ctk.END)
    apadrinhadaComboboxPadrinho.set('')

# Botão Salvar da janela cadastro criança
def salvarCriancas():
    nome = nomeEntryCrianca.get()
    responsavel = responsavelEntryCrianca.get()
    idade = idadeComboboxCrianca.get()
    endereco = enderecoEntryCrianca.get()
    contato = telefoneEntryCrianca.get()
    genero = generoVar.get() 
    
    conexao = conectarDb()
    if conexao is not None:
        adicionarCriancas(conexao, nome, responsavel, endereco, contato, idade, genero)
        # Paea limpar os campos após salvar os dados
        limpaCamposCrianca()
        desconectarDb(conexao)
        
# Botão Salvar da janela cadastro padrinho
def salvarPadrinhos():
    nome = nomeEntryPadrinho.get()
    contato = telefoneEntryPadrinho.get()
    email = emailEntryPadrinho.get()
    endereco = enderecoEntryPadrinho.get()
    criancaApadrinhada = apadrinhadaComboboxPadrinho.get()

    conexao = conectarDb()
    if conexao is not None:
        try: 
            idCriancaSelcionada = obterCriancaPorNome(conexao, criancaApadrinhada)
            adicionarPadrinhos(conexao, nome, contato, email, endereco, idCriancaSelcionada)
            # Paea limpar os campos após salvar os dados
            limpaCamposPadrinho()
        except Exception as e:
            print(f"Erro ao salvar padrinho: {e}")
        finally:    
            desconectarDb(conexao)
            
# Para pegar o id da criança atraves do nome que foi colocado na combobox
def listaNomesCriancas():
    conexao = conectarDb()
    if conexao is None:
        print("Erro ao conectar com o banco de dados!")
        return []
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM criancas")
        nomeCriancas = [row[0] for  row in cursor.fetchall()]
        cursor.close()
        return nomeCriancas
    except Exception as e:
        print("Erro ao carregar nomes das crianças: {e}")
        return []
    finally:
        desconectarDb(conexao)

# Cria uma tabela com treview e pega todos os dados da tabela crianças
def exibirDadosCriancas():
    conexao = conectarDb()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, idade, responsavel, endereco, contato, genero FROM criancas ORDER BY nome ASC")
            dados = cursor.fetchall() 
            
            # Criando o treeview para mostrar os dados
            global tabelaCriancas
            tabelaCriancas = ttk.Treeview(dadosCriancas, columns=('Nome', 'Idade', 'Responsável', 'Endereço', 'Contato', 'Gênero'), show='headings')
            tabelaCriancas.heading('Nome', text='Nome')
            tabelaCriancas.heading('Idade', text='Idade')
            tabelaCriancas.heading('Responsável', text='Responsável')
            tabelaCriancas.heading('Endereço', text='Endereço')
            tabelaCriancas.heading('Contato', text='Contato')
            tabelaCriancas.heading('Gênero', text='Gênero')

            # Definir a largura das colunas
            tabelaCriancas.column('Nome', width=100)
            tabelaCriancas.column('Idade', width=65)
            tabelaCriancas.column('Responsável', width=100)
            tabelaCriancas.column('Endereço', width=150)
            tabelaCriancas.column('Contato', width=100)
            tabelaCriancas.column('Gênero', width=65)

            tabelaCriancas.place(relx=0.10, rely=0.4, relwidth=0.86, relheight=0.50)


            # Criando a barra de rolagem
            barraRolar = ttk.Scrollbar(dadosCriancas, orient="vertical", command=tabelaCriancas.yview)

            # Definindo que a barra pertence à tabela
            tabelaCriancas.configure(yscrollcommand=barraRolar.set)
            barraRolar.place(relx=0.96, rely=0.4, relwidth=0.03, relheight=0.50)

            # Inserir os dados nas colunas
            for linha in dados:
                tabelaCriancas.insert('', 'end', values=linha)
                
            cursor.close()
        except Exception as e:
            print(f"Erro ao exibir os dados das crianças: {e}")
        finally:
            desconectarDb(conexao)

# Cria uma tabela com treview e pega todos os dados da tabela padrinhos
def exibirDadosPadrinhos():
    conexao = conectarDb()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, telefone, email, endereco FROM padrinhos ORDER BY nome ASC")
            dados = cursor.fetchall()
            
            # Criando o Treeview
            global tabelaPadrinhos
            tabelaPadrinhos = ttk.Treeview(dadosPadrinhos, columns=('Nome', 'Telefone', 'Email', 'Endereço'), show='headings')
            tabelaPadrinhos.heading('Nome', text='Nome')
            tabelaPadrinhos.heading('Telefone', text='Telefone')
            tabelaPadrinhos.heading('Email', text='Email')
            tabelaPadrinhos.heading('Endereço', text='Endereço')
        
            # Definir a largura das colunas
            tabelaPadrinhos.column('Nome', width=100)
            tabelaPadrinhos.column('Telefone', width=65)
            tabelaPadrinhos.column('Email', width=100)
            tabelaPadrinhos.column('Endereço', width=150)

            tabelaPadrinhos.place(relx=0.10, rely=0.4, relwidth=0.86, relheight=0.50)

            # Criando a barra de rolagem
            barraRolar = ttk.Scrollbar(dadosPadrinhos, orient="vertical", command=tabelaPadrinhos.yview)

            # Definindo que a barra pertence à tabela
            tabelaPadrinhos.configure(yscrollcommand=barraRolar.set)
            barraRolar.place(relx=0.96, rely=0.4, relwidth=0.03, relheight=0.50)

            # Inserindo dados no Treeview
            for linha in dados:
                tabelaPadrinhos.insert('', 'end', values=linha)
 
            cursor.close()
        except Exception as e:
            print(f"Erro ao exibir dados dos padrinhos: {e}")
        finally:
            desconectarDb(conexao)
# Botão atulizar tabela das crianças
def atualizarDadosCrianca():
    # limpa a tabela para depois atualizar com novos dados
    tabelaCriancas.delete(*tabelaCriancas.get_children())
    
    conexao = conectarDb()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, idade, responsavel, endereco, contato, genero FROM criancas ORDER BY nome ASC")
            dados = cursor.fetchall()
            
            for linha in dados:
                tabelaCriancas.insert("", ctk.END, values=linha)
        except Exception as e:
            print(f"Erro ao carregar as crianças: {e}")
        finally:
            desconectarDb(conexao)

# Botão atulizar tabela das padrinhos
def atualizarDadosPadrinhos():
    tabelaPadrinhos.delete(*tabelaPadrinhos.get_children())
    conexao = conectarDb()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, telefone, email, endereco FROM padrinhos ORDER BY nome ASC")
            dados = cursor.fetchall()
            
            for linha in dados:
                tabelaPadrinhos.insert('', ctk.END, values=linha)
        except Exception as e:
            print(f"Erro ao carregar crianças: {e}")
        finally:
            desconectarDb(conexao)

# Botão excluir nome da tabela das crianças
def excluirCrianca():
    # Verifica se tem criança seçecionada na tabela
    criancaSelecionada = tabelaCriancas.selection()
    if not criancaSelecionada:
        print("Nenhuma criança selecionada.")
        return
    
    # Faz uma iteração ate chegar na criança desejada e pega os valores dessa criança
    for item in criancaSelecionada:
        valores = tabelaCriancas.item(item, 'values')
        nomeCrianca = valores[0]
    
    # Aviso se realmente quer excluir 
    Aviso = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {nomeCrianca}")
    
    # Conexão com o bd e deleta o nome selecionado do bd
    if Aviso:
        try:
            conexao = conectarDb()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM criancas WHERE nome = %s", (nomeCrianca,))
            conexao.commit()
            
            # Tá excluindo da tabela que visualizamos na interface
            tabelaCriancas.delete(criancaSelecionada)
        except Exception as e:
            print(f"Erro ao excluir {nomeCrianca}, {e}")
        finally:
            desconectarDb(conexao)

# Botão excluir nome da tabela das padrinhos
def excluirPadrinho():
    padrinhoSelecionado = tabelaPadrinhos.selection()
    if not padrinhoSelecionado:
        print("Nenhum padrinho selecionado!")
        return
    for item in padrinhoSelecionado:
        valores = tabelaPadrinhos.item(item, 'values')
        nomePadrinho = valores[0]
    
    aviso = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {nomePadrinho}")
    
    try:
        conexao = conectarDb()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM padrinhos WHERE nome = %s", (nomePadrinho,))
        conexao.commit()
        tabelaPadrinhos.delete(padrinhoSelecionado)
    except Exception as e:
            print(f"Erro ao excluir {nomePadrinho}, {e}")
    finally:
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
    exibirDadosCriancas()
    
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
    nomeEntryCrianca.place(x=315, y=215)
   
    # Botão buscar crianças
    botaoBuscar = ctk.CTkButton(dadosCriancas, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoBuscar.place(x=538, y=215)
    
    # Botão excluir crianças
    botaoExcluir = ctk.CTkButton(dadosCriancas, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command=excluirCrianca)
    botaoExcluir.place(x=477, y=660)
   
    # Botão Editar crianças
    botaoEditar = ctk.CTkButton(dadosCriancas, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoEditar.place(x=398, y=660)
   
    # Botão atualizar crianças
    botaoAtualizar = ctk.CTkButton(dadosCriancas, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command= atualizarDadosCrianca)
    botaoAtualizar.place(x=555, y=660)
    
    # Botão Cadastrar crianças
    botaoCadastro = ctk.CTkButton(dadosCriancas, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
    botaoCadastro.place(x=310, y=660)
    botaoCadastro.bind("<Button-1>", lambda e: janelaCadastro())
    
    # Jamela de cadastro de mais crianças, ao clicar no botão cadastrar vai abrir essa tela
    def janelaCadastro():
        # Configurações da janela
        global cadastroCrianca, nomeEntryCrianca, responsavelEntryCrianca, idadeComboboxCrianca, enderecoEntryCrianca, telefoneEntryCrianca, generoVar
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

        # Variável que armazenará o valor do gênero selecionado
        generoVar = tk.StringVar(value="Masculino")  # Valor inicial padrão

        # Opção Masculino
        masculinoRadio = ctk.CTkRadioButton(cadastroCrianca, text="Masculino", variable=generoVar, value="Masculino", font=("Georgia", 12))
        masculinoRadio.place(x=230, y=320)

        # Opção Feminino
        femininoRadio = ctk.CTkRadioButton(cadastroCrianca, text="Feminino", variable=generoVar, value="Feminino", font=("Georgia", 12))
        femininoRadio.place(x=325, y=320)
       
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
        exibirDadosPadrinhos()
        
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
        nomeEntryPadrinho = ctk.CTkEntry(dadosPadrinhos, placeholder_text="Inserir o nome", font=("Georgia", 12), width=200)
        nomeEntryPadrinho.place(x=317, y=215)
    
        # Botão buscar padrinhos
        botaoBuscar = ctk.CTkButton(dadosPadrinhos, text="Buscar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoBuscar.place(x=533, y=215)
        
        # Botão excluir padrinhos
        botaoExcluir = ctk.CTkButton(dadosPadrinhos, text="Excluir", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command=excluirPadrinho)
        botaoExcluir.place(x=565, y=660)
    
        # Botão Editar padrinhos
        botaoEditar = ctk.CTkButton(dadosPadrinhos, text="Editar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoEditar.place(x=405, y=660)
    
        # Botão atualizar padrinhos
        botaoAtualizar = ctk.CTkButton(dadosPadrinhos, text="Atualizar", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command=atualizarDadosPadrinhos)
        botaoAtualizar.place(x=485, y=660)
        
        # Botão Cadastrar padrinhos
        botaoCadastro = ctk.CTkButton(dadosPadrinhos, text="Cadastrar", fg_color="orange", text_color="white", hover_color="darkorange", width=60)
        botaoCadastro.place(x=315, y=660)
        botaoCadastro.bind("<Button-1>", lambda e: cadastroPadrinhos())

        def cadastroPadrinhos():
            # Configurações da janela
            global dadoscadastroPadrinho, nomeEntryPadrinho, telefoneEntryPadrinho, emailEntryPadrinho, criancaEntryPadrinho, enderecoEntryPadrinho, apadrinhadaComboboxPadrinho
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
        
            # Endereço padrinho
            enderecoLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Endereço: ", font=("Georgia", 12))
            enderecoLabelPadrinho.place(x=20, y=270)
            enderecoEntryPadrinho = ctk.CTkEntry(dadoscadastroPadrinho, placeholder_text="Nome do endereço", font=("Georgia", 12), width=260)
            enderecoEntryPadrinho.place(x=165, y=270)

            # Criança apadrinhada
            apadrinhadaLabelPadrinho = ctk.CTkLabel(dadoscadastroPadrinho, text="Criança Apadrinhada: ", font=("Georgia", 12))
            apadrinhadaLabelPadrinho.place(x=20, y=330) 
            listaCrianca = listaNomesCriancas()
            apadrinhadaComboboxPadrinho = ctk.CTkComboBox(dadoscadastroPadrinho, values=listaCrianca, font=("Georgia", 12), width=260, state="normal" )
            apadrinhadaComboboxPadrinho.set('')
            apadrinhadaComboboxPadrinho.place(x=165, y=330)
            
            # Botão Salvar padrinhos 
            botaoSalvar = ctk.CTkButton(dadoscadastroPadrinho, text="Salvar", fg_color="orange", text_color="white", hover_color="darkorange", width=60, command= salvarPadrinhos)
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