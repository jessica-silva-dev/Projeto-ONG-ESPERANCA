import mysql.connector
from mysql.connector import Error

# Conectando ao banco de dados
# Antes faça o passo a passo no worbench, está no grupo!
# Crie sua branch 
def conectarDb():
    # Essa try é como se eu falo tenta fazer isso (no caso o que está dentro do bloco que é a conexão com o banco)
    try:
        conexao = mysql.connector.connect(
            host='192.168.1.14',        
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

# Verifica a conexão, não vamos ficar 
# usando assim isso é só pra ver no terminal que está funcionando.
#con = conectarDb()
#desc = desconectarDb(con)

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
        
# Adicionar crianças no banco de dados
def adicionarCriancas(conexao, nome, idade, responsavel, endereco, contato, genero):
    try:
        cursor = conexao.cursor()
        comandoSql = """ INSERT INTO criancas (nome, idade, responsavel, endereco, contato, genero)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (nome, responsavel, idade, endereco, contato, genero)
        cursor.execute(comandoSql, valores)
        conexao.commit()
        print(f"Criança: {nome} adicionada com sucesso!")
        cursor.close()
    except Error as e:
        print(f"Erro ao adicionar a criança: {e}")

def adicionarPadrinhos(conexao, nome, telefone, email, endereco ):
    try:
        cursor = conexao.cursor()
        comandosql = """ INSERT INTO padrinhos (nome, telefone, email, endereco )
                        VALUES (%s, %s, %s, %s)"""
        valores = (nome, telefone, email, endereco)
        cursor.execute(comandosql, valores)
        conexao.commit()
        print(f"Padrinho: {nome} adicionada com sucesso!")
        cursor.close()
    except Error as e:
        print(f"Erro ao adicionar o Padrinho: {e}")