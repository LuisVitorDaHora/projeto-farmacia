#Bibliotecas
import mysql.connector
from mysql.connector import Error

#Função para criar a conexão com o banco de dados MySQL
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',         # ou IP do servidor MySQL
            user='root',       # substitua pelo seu usuário do MySQL
            password='3501',     # substitua pela sua senha
            database='farmacia'     # substitua pelo nome do seu banco
        )
        # Verifica se a conexão foi bem-sucedida
        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return conexao
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
