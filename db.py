import mysql.connector
from mysql.connector import Error

# Conectando ao banco de dados
def conectarDb():
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
        