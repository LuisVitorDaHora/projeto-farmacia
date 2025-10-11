#Bibliotecas
from db_config import criar_conexao
from datetime import datetime

#Funções para o sistema de produtos
#Cadastro de produtos
def cadastrar_produto():
   nome = input ('Nome do produto: ')
   preco = float (input('Preço do produto: '))
   descricao = input('Digite a descrição: ')
   validade = input('Data de validade (YYYY/MM/DD HH:MM:SS): ')

   conexao = criar_conexao()
   cursor = conexao.cursor()

   comando = """ 
      INSERT INTO tbl_produtos(nome_produtos,preco_produtos,descricao_produtos,dt_validade_produtos)
      VALUES (%s,%s,%s,%s)
   """
   cursor.execute(comando,(nome,preco,descricao,validade))
   conexao.commit()
   
   cursor.close()
   conexao.close()
   print (f'Produto {nome} foi cadastrado com sucesso')

#Listar produtos
def listar_produtos():
   conexao = criar_conexao()
   cursor = conexao.cursor(dictionary=True)
   cursor.execute("SELECT * FROM tbl_produtos ORDER BY id_produtos")
   produtos = cursor.fetchall()
   cursor.close()
   conexao.close()

   print ("\n Lista de produtos: ")
   if not produtos:
      print('Nenhum produto cadastrado: ')
   else:
      for p in produtos:
         print(f"ID: {p['id_produtos']} | {p['nome_produtos']} - R${p['preco_produtos']:.2f} | validade: {p['dt_validade_produtos']}")

#Atualizar produtos
def atualizar_produtos():
   idp = int (input('Id do produto: '))
   nome_produtos = (input('Digite o nome do produto: '))
   preco_produtos = float (input('Digite o novo preço do produto: '))
   descriçao_produtos = input('Digite a descrição do produto: ')
   data_validade = input ('Digite a data de validade (YYYY/MM/DD HH:MM:SS): ')

   conexao = criar_conexao()
   cursor = conexao.cursor()
   cursor.execute('UPDATE tbl_produtos SET nome_produtos = %s,preco_produtos = %s, descricao_produtos = %s, dt_validade_produtos = %s WHERE id_produtos = %s',(nome_produtos,preco_produtos,descriçao_produtos,data_validade,idp))
   conexao.commit()
   cursor.close()
   conexao.close()
   print(f'Produto ID {idp} atualizado com sucesso!')

#Excluir produto
def excluir_produto():
    idp = int(input("ID do produto a excluir: "))

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_produtos WHERE id_produtos = %s", (idp,))
    produto = cursor.fetchone()
    if produto is None:
        print(f"Nenhum produto encontrado com ID {idp}.")
    else:
        cursor.execute("DELETE FROM tbl_produtos WHERE id_produtos = %s", (idp,))
        conexao.commit()
        print(f" Produto ID {idp} removido com sucesso.")
    
    cursor.close()
    conexao.close()

#Funções para o sistema de funcionários
#Cadastro de funcionarios
def cadastrar_funcionarios():
   nome_func = input('Coloque o nome do funcionario: ')
   cpf_func = input('Coloque o cpf do funcionario: ')
   cargo_func = input ('Coloque o cargo do funcionario: ')

   conexao = criar_conexao()
   cursor = conexao.cursor()
   comando = """ 
      INSERT INTO tbl_funcionarios(nome_funcionarios, cpf_funcionarios, cargo_funcionarios)
      VALUES (%s,%s,%s)
   """
   cursor.execute(comando,(nome_func,cpf_func,cargo_func))
   conexao.commit()
   cursor.close()
   conexao.close()
   print (f'O Funcionario {nome_func} foi cadastrado com sucesso!')

#Listar funcionarios
def listar_funcionarios():
   conexao = criar_conexao()
   cursor = conexao.cursor(dictionary=True)
   cursor.execute("SELECT * FROM tbl_funcionarios ORDER BY id_funcionarios")
   funcionarios = cursor.fetchall()
   cursor.close()
   conexao.close()

   print ("\n Lista de funcinarios: ")
   if not funcionarios:
      print('Nenhum funcionario cadastrado: ')
   else:
      for f in funcionarios:
         print (f'ID: {f['id_funcionarios']}|{f['nome_funcionarios']} - {f['cpf_funcionarios']}|{f['cargo_funcionarios']}')

#Atualizar cargo do funcionario
def atualizar_funcionarios():
    idf = int (input('Id do funcionario: '))
    novo_cargo = input ('Novo cargo: ')
    nome_func = input ('Nome novo do funcinario: ')
    cpf_func = input ('CPF novo do funcionario: ')

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("UPDATE tbl_funcionarios SET nome_funcionarios = %s, cpf_funcionarios = %s, cargo_funcionarios = %s WHERE id_funcionarios = %s", (nome_func, cpf_func, novo_cargo, idf))
    conexao.commit()

    print(f' Funcionario ID {idf} atualizado com sucesso!')
    cursor.close()
    conexao.close()


#Excluir funcionario
def excluir_funcionarios():
    idf = int(input("ID do funcionario a excluir: "))

    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tbl_funcionarios WHERE id_funcionarios = %s", (idf,))
    funcionario = cursor.fetchone()

    if funcionario is None:
        print(f"Nenhum funcionario encontrado com ID {idf}.")
    else:
        cursor.execute("DELETE FROM tbl_funcionarios WHERE id_funcionarios = %s", (idf,))
        conexao.commit()
        print(f"ID Funcionario {idf} removido com sucesso.")
    
    cursor.close()
    conexao.close()

#Funções para o sistema de fornecedores
#Cadastro de fornecedores
def cadastrar_fornecedor():
    nome_fornecedor = input("Nome do fornecedor: ")
    contato_fornecedor = input("Número do fornecedor: ")
    
    conexao = criar_conexao()
    cursor = conexao.cursor()
    comando = """ 
        INSERT INTO tbl_fornecedor (nome_fornecedor, contato_fornecedor)
        VALUES (%s, %s)
    """
    cursor.execute(comando, (nome_fornecedor, contato_fornecedor))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Fornecedor '{nome_fornecedor}' cadastrado com sucesso!")

#Listar fornecedores
def listar_fornecedor():
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_fornecedor")
    fornecedores = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("\n=== Lista de Fornecedores ===")
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
    else:
        for f in fornecedores:
            print(f"ID: {f['id_fornecedor']} | Nome: {f['nome_fornecedor']} | Contato: {f['contato_fornecedor']}")

#Atualizar número do fornecedor
def atualizar_fornecedor():
    idfo = int(input("ID do fornecedor: "))
    nome_fornecedor = input("Nome do fornecedor: ")
    novo_numero = input("Novo número de contato: ")
    
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_fornecedor SET nome_fornecedor = %s, contato_fornecedor = %s WHERE id_fornecedor = %s", (nome_fornecedor, novo_numero, idfo))
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f" Fornecedor ID {idfo} atualizado com sucesso")

#Excluir fornecedor
def excluir_fornecedor():
    idfo = int(input("ID do fornecedor a excluir: "))

    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_fornecedor WHERE id_fornecedor = %s", (idfo,))
    fornecedor = cursor.fetchone()

    if fornecedor is None:
        print(f" Nenhum fornecedor encontrado com o ID {idfo}.")
    else:
        cursor.execute("DELETE FROM tbl_fornecedor WHERE id_fornecedor = %s", (idfo,))
        conexao.commit()
        print(f" Fornecedor ID {idfo} removido com sucesso.")

    cursor.close()
    conexao.close()

#Funções para o sistema de estoque
#Cadastrar estoque
def cadastrar_estoque():
    qtde = int (input('Quantidade do produto: '))
    lote = input ('Lote do produto: ')

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute ( """
        INSERT INTO tbl_estoque(qtde_estoque,lote_estoque)
        VALUES (%s,%s)
    """, (qtde,lote))
    conexao.commit()
    cursor.close()
    conexao.close()
    print (f'Estoque do produto {lote} cadastrado com sucesso')

#Listar estoque
def listar_estoque():
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_estoque ORDER BY id_estoque")
    estoques = cursor.fetchall()
    cursor.close()
    conexao.close()

    print ("\n Lista de estoque: ")
    if not estoques:
       print('Nenhum estoque cadastrado: ')
    else:
       for e in estoques:
          print (f'ID: {e['id_estoque']}|{e['qtde_estoque']} - {e['lote_estoque']}')

#Atualizar estoque
def atualizar_estoque():
    id_estoque = int(input("ID do estoque: "))
    novo_lote = (input("Novo lote: "))

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tbl_estoque SET lote_estoque = %s WHERE id_estoque = %s", (novo_lote, id_estoque))
    conexao.commit()
    if cursor.rowcount == 0:
        print(" ID não encontrado.")
    else:
        print(" Quantidades atualizadas com sucesso.")
    cursor.close()
    conexao.close()

#Excluir estoque
def excluir_estoque():
    id_estoque = int(input("ID do estoque a excluir: "))

    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_estoque WHERE id_estoque = %s", (id_estoque,))
    estoque = cursor.fetchone()

    if estoque is None:
        print(f" Nenhum estoque encontrado com o ID {id_estoque}.")
    else:
        cursor.execute("DELETE FROM tbl_estoque WHERE id_estoque = %s", (id_estoque,))
        conexao.commit()
        print(f" Estoque ID {id_estoque} removido com sucesso.")

    cursor.close()
    conexao.close()

#Cadastrar entrada no estoque
def cadastrar_entrada_estoque():
    id_estoque = int(input("ID do estoque: "))
    quantidade = int(input("Quantidade de entrada: "))
    data_entrada = datetime.now()

    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        # Registrar a entrada
        cursor.execute("""
            INSERT INTO tbl_entrada_estoque (data_entrada, quantidade_entrada)
            VALUES (%s, %s)
        """, (data_entrada, quantidade))
        
        # Atualizar a quantidade no estoque
        cursor.execute("""
            UPDATE tbl_estoque
            SET qtde_estoque = qtde_estoque + %s
            WHERE id_estoque = %s
        """, (quantidade, id_estoque))

        conexao.commit()
        print(f"Entrada de {quantidade} unidades registrada no estoque ID {id_estoque} com sucesso.")
    except Exception as e:
        print("Erro ao registrar entrada:", e)
    finally:
        cursor.close()
        conexao.close()

def listar_entradas_estoque():
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_entrada_estoque ORDER BY id_entrada DESC")
    entradas = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("\n=== LISTA DE ENTRADAS DE ESTOQUE ===")
    if not entradas:
        print("Nenhuma entrada registrada.")
    else:
        for e in entradas:
            print(f"ID: {e['id_entrada']} | Data: {e['data_entrada']} | Quantidade: {e['quantidade_entrada']}")

#Cadastrar saída no estoque
def cadastrar_saida_estoque():
    id_estoque = int(input("ID do estoque: "))
    quantidade = int(input("Quantidade de saída: "))
    data_saida = datetime.now()

    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        # Verifica a quantidade disponível
        cursor.execute("SELECT qtde_estoque FROM tbl_estoque WHERE id_estoque = %s", (id_estoque,))
        resultado = cursor.fetchone()
        if not resultado:
            print("Estoque não encontrado.")
            return

        qtde_atual = resultado[0]
        if quantidade > qtde_atual:
            print(f"Quantidade insuficiente. Estoque atual: {qtde_atual}")
            return

        # Registrar saída
        cursor.execute("""
            INSERT INTO tbl_saida_estoque (data_saida, quantidade_saida)
            VALUES (%s, %s)
        """, (data_saida, quantidade))

        # Atualizar o estoque
        cursor.execute("""
            UPDATE tbl_estoque
            SET qtde_estoque = qtde_estoque - %s
            WHERE id_estoque = %s
        """, (quantidade, id_estoque))

        conexao.commit()
        print(f"Saída de {quantidade} unidades registrada no estoque ID {id_estoque} com sucesso.")
    except Exception as e:
        print("Erro ao registrar saída:", e)
    finally:
        cursor.close()
        conexao.close()

def listar_saidas_estoque():
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_saida_estoque ORDER BY id_saida DESC")
    saidas = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("\n=== LISTA DE SAÍDAS DE ESTOQUE ===")
    if not saidas:
        print("Nenhuma saída registrada.")
    else:
        for s in saidas:
            print(f"ID: {s['id_saida']} | Data: {s['data_saida']} | Quantidade: {s['quantidade_saida']}")


#Menus
#Menu de produtos
def menu_produtos():
   while True:
      print ('\n === SISTEMA DE ESTOQUE PRODUTOS - FARMATECH ===')
      print ('1 - Cadastrar produtos')
      print ('2 - Listar produtos')
      print ('3 - Atualizar produtos')
      print ('4 - Excluir produtos')
      print ('0 - Sair')
      
      opcao = input('Escolha uma opção: ')

      if opcao == '1':
         cadastrar_produto()
      elif opcao == '2':
         listar_produtos()
      elif opcao == '3':   
        atualizar_produtos()
      elif opcao == '4':
         excluir_produto()
      elif opcao == '0':

         print('Encerrando sistema produtos...')
         break
      else:
         print('Opção invalidade, escolha a opção entre 1 a 4 ou 0 para sair')

#Menu de funcionários
def menu_funcionarios():
    while True:
       print ('\n === SISTEMA DE ESTOQUE FUNCIONARIOS - FARMATECH ===')
       print ('1 - Cadastrar Funcionarios')
       print ('2 - Listar Funcionarios')
       print ('3 - Atualizar Funcionarios')
       print ('4 - Excluir funcionarios')
       print ('0 - Sair')

       opcao = input('Escolha uma opção: ')
       if opcao == '1':
         cadastrar_funcionarios()
       elif opcao == '2':
         listar_funcionarios()
       elif opcao == '3':
            atualizar_funcionarios()
       elif opcao == '4':
         excluir_funcionarios()
       elif opcao == '0':
      
         print('Encerrando sistema funcionarios...')
         break
       else:
          print('Opção invalidade, escolha a opção entre 1 a 4 ou 0 para sair')

#Menu fornecedor
def menu_fornecedor():
    while True:
        print("\n=== SISTEMA DE FORNECEDORES - FARMATECH ===")
        print("1 - Cadastrar fornecedor")
        print("2 - Listar fornecedores")
        print("3 - Atualizar fornecedor")
        print("4 - Excluir fornecedor")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_fornecedor()
        elif opcao == '2':
            listar_fornecedor()
        elif opcao == '3':
            atualizar_fornecedor()
        elif opcao == '4':
            excluir_fornecedor()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print('Opção invalidade, escolha a opção entre 1 a 4 ou 0 para sair')

#Menu estoque
def menu_estoque():
    while True:
        print("\n=== SISTEMA DE ESTOQUE - FARMATECH ===")
        print("1 - Cadastrar estoque")
        print("2 - Listar estoque")
        print("3 - Atualizar estoque")
        print("4 - Excluir estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_estoque()
        elif opcao == '2':
            listar_estoque()
        elif opcao == '3':
            atualizar_estoque()
        elif opcao == '4':
            excluir_estoque()
        elif opcao == '0':
            print("Encerrando o sistema de estoque...")
            break
        else:
            print('Opção invalidade, escolha a opção entre 1 a 4 ou 0 para sair')

def menu_entrada_saida_estoque():
    while True:
        print("\n=== MENU DE ENTRADA E SAÍDA DE ESTOQUE - FARMATECH ===")
        print("1 - Registrar entrada de estoque")
        print("2 - Registrar saída de estoque")
        print("3 - Listar entradas de estoque")
        print("4 - Listar saídas de estoque")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_entrada_estoque()
        elif opcao == '2':
            cadastrar_saida_estoque()
        elif opcao == '3':
            listar_entradas_estoque()
        elif opcao == '4':
            listar_saidas_estoque()
        elif opcao == '0':
            print("Voltando ao menu principal...")
            break
        else:
            print('Opção invalidade, escolha a opção entre 1 a 4 ou 0 para sair')


#Menu principal
def menu_principal():
    while True:
       print ('\n === SISTEMA DE ESTOQUE MENU PRINCIPAL - FARMATECH ===')
       print('1 - Menu Produtos')
       print('2 - Menu Funcionarios')
       print('3 - Menu Fornecedores')
       print('4 - Menu Estoque')
       print('5 - Menu Entrada/Saída Estoque')
       print('0 - Sair')

       opcao = input('Escolha uma opção: ')

       if opcao == '1':
          menu_produtos()
       elif opcao == '2':
          menu_funcionarios()
       elif opcao == '3':
          menu_fornecedor()
       elif opcao == '4':
            menu_estoque()
       elif opcao == '5':
            menu_entrada_saida_estoque()
       elif opcao == '0':
          print('Encerrando o sistema...')
          break
       else:
         print('opção invalidade, escolha 1 a 5 ou 0 para sair')

#Iniciar o sistema
if __name__ == "__main__":
    menu_principal()
