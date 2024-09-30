import mysql.connector
from mysql.connector import Error

# Conectando ao banco de dados
# Antes faça o passo a passo no worbench, está no grupo!
# Crie sua branch 
def conectarDb():
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
con = conectarDb()
desc = desconectarDb(con)
        