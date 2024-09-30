import mysql.connector
from mysql.connector import Error

def conectarDb():
    conexao = mysql.connector.connect(
        host='localhost',
        database="esperanca",
        user="dev",
        password="Esperanca@2024"
    )
    return conexao

conectar = conectarDb()
if conectar.is_connected():
    print("Conectado com sucesso!")
else:
    print("Erro ao se conectar!")

def desconectarDb():
    if conectar.is_connected():
        conectar.close()
        print("Desconectado com sucesso!")
        



    
