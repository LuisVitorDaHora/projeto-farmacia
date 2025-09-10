#Bibliotecas
from db_config import criar_conexao

# Testando a conexão
conexao = criar_conexao()

# Exemplo simples de uso da conexão
if conexao:
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Tabelas no banco:", tabelas)
    conexao.close()

