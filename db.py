import mysql.connector
from mysql.connector import Error

# Conectando ao banco de dados
# Antes faça o passo a passo no worbench, está no grupo!
# Crie sua branch 
def conectarDb():
    # Essa try é como se eu falo tenta fazer isso (no caso o que está dentro do bloco que é a conexão com o banco)
    try:
        conexao = mysql.connector.connect(
            host='localhost',        
            database="esperanca",
            user="dev",
            password="Esperanca@2024"
        )
        if conexao.is_connected():
            print("Conectado com sucesso!")
            return conexao
    except Error as e:
        print(f"Erro ao se conectar: {e}")
        return None

# Desconectando do banco de dados
def desconectarDb(conexao):
    if conexao.is_connected():
        conexao.close()
        print("Desconectado com sucesso!")

# Criando as tabelas
def criarTabelas(conexao):
    try:
        cursor = conexao.cursor()
        
        # Tabela das crianças
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS criancas (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL,
            responsavel VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            contato VARCHAR(20) NOT NULL,
            genero ENUM('Masculino', 'Feminino') NOT NULL,
            PRIMARY KEY (id)
        )
        """)
        
        # Tabela das crianças
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS padrinhos (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            telefone VARCHAR(20),
            endereco VARCHAR(255),
            PRIMARY KEY (id)
        )
        """)
        
        # Tabela  das crianças e padrinhos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS criancas_padrinhos (
            id_crianca INT,
            id_padrinho INT,
            PRIMARY KEY (id_crianca, id_padrinho),
            FOREIGN KEY (id_crianca) REFERENCES criancas(id) ON DELETE CASCADE,
            FOREIGN KEY (id_padrinho) REFERENCES padrinhos(id) ON DELETE CASCADE
        )
        """)
        print("Tabelas criadas!")
        cursor.close()
    except Error as e:
        print(f"Erro ao criar as tabelas: {e}")
        
# Para criar as tabelas no workbench 
#conexao = conectarDb()
#if conexao.is_connected():
#    criarTabelas(conexao)
#    desconectarDb(conexao)
    
# Adicionar crianças no banco de dados
def adicionarCriancas(conexao, nome, responsavel, endereco, contato, idade, genero):
    try:
        cursor = conexao.cursor()
        comandoSql = """ INSERT INTO criancas (nome, responsavel, endereco, contato, idade, genero)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (nome, responsavel, endereco, contato, idade, genero)
        cursor.execute(comandoSql, valores)
        conexao.commit()
        print(f"Criança: {nome} adicionada com sucesso!")
        cursor.close()
    except Error as e:
        print(f"Erro ao adicionar a criança: {e}")
        
# Associar criança ao Padrinho por nome
def obterCriancaPorNome(conexao, criancaApadrinhada):
    cursor = conexao.cursor()
    comandoSql = "SELECT id FROM criancas WHERE nome = %s"
    cursor.execute(comandoSql, (criancaApadrinhada,))
    resultado = cursor.fetchone()
    cursor.close()
    
    if resultado:
        return resultado[0]
    else:
        return None

    
# Adicionar padrinhos no banco de dados
def adicionarPadrinhos(conexao, nome, telefone, email, endereco, idCriancaSelcionada ):
    try:
        cursor = conexao.cursor()
        comandosql = """ INSERT INTO padrinhos (nome, telefone, email, endereco )
                        VALUES (%s, %s, %s, %s)"""
        valores = (nome, telefone, email, endereco)
        cursor.execute(comandosql, valores)
        conexao.commit()
        id_padrinho = cursor.lastrowid
        
        if idCriancaSelcionada:
            adicionarCriancaPadrinhos(conexao, idCriancaSelcionada, id_padrinho)
            
        print(f"Padrinho: {nome} adicionada com sucesso!")
        cursor.close()
    except Error as e:
        print(f"Erro ao adicionar o Padrinho: {e}")
        
# Adicionar na tabela criança e padrinho no banco de dados
def adicionarCriancaPadrinhos(conexao, id_crianca, id_padrinho):
    try:
        cursor = conexao.cursor()
        comandoSql = """ INSERT INTO criancas_padrinhos (id_crianca, id_padrinho)
                        VALUES (%s, %s)"""
        valores = (id_crianca, id_padrinho)
        cursor.execute(comandoSql, valores)
        conexao.commit()
        print(f"Criança com o id {id_crianca} associada ao Padrinho com o id {id_padrinho}")
        cursor.close()
    except Error as e:
        print(f"Erro ao associar a criança ao Padrinho! {e}")
        
# Se precisar fazer alterações ou adicionar tabelas, colunas, campos ...
# Com essa função dá para alterar pelo proprio python, ao invés de usar o workbench 
# Apenas adicionando na variável comandoSql os comando SQL que vc quer 
# Tire a parte de baixo os "#" e é para ser execuado as alteraçções. 
# Faça isso ma sua branch por favor, não se esqueça.

def fazerAlteracoesNoBanco(conexao, comandoAql):
    try:
        cursor = conexao.cursor()
        cursor.execute(comandoAql)
        conexao.commit()
        print("Alteração adicionada com sucesso")
        cursor.close()
    except Error as e:
        print(f"Erro ao alterar: {e}")

#conexao = conectarDb()
#if conexao.is_connected:
#    comandoSql = "Coloque a sua alteração aqui!"
#    fazerAlteraçõesNoBanco(conexao, comandoSql)