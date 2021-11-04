from cliente import Cliente
from motocicleta import Motocicleta


def deletar():
    print(f'''\n************ DELETAR REGISTRO ************

    Selecione a tabela:
    1 - CLIENTE
    2 - MOTOCICLETA

''')

    table = int(input(f'>> ').strip())
    cod = input('>> Digite o código do registro: ')
    conn = Cliente() if table == 1 else Motocicleta()

    try:
        conn.delete(cod)

    except Exception as e:  
        print('Não foi possível deletar o registro!')
        




def cadastrar(table):
    print(f'''\n************ CADASTRAR {'CLIENTE' if table == 1 else 'VEÍCULO'} ************
''')

    if table == 1:
        nome = input(">> NOME: ")
        telefone = input(">> TELEFONE: ")
        email = input(">> EMAIL: ")
        cpf = input(">> CPF: ")
        item = Cliente()

        try:
            item.insert(nome, telefone, email, cpf)
            print("\nCliente cadastrado com sucesso!")

        except Exception as e:
            print("\nNão foi possível cadastrar o cliente.")

    if table == 2:
        cod = input(">> CÓDIGO: ")
        modelo = input(">> MODELO: ")
        valor = float(input(">> VALOR: ").strip())
        qtd_estoque = int(input(">> QTD ESTOQUE: ").strip())
        item = Motocicleta()

        try:
            item.insert(cod, modelo, valor, qtd_estoque)
            print("\nVeículo registrado com sucesso!")

        except Exception as e:
            print("\nNão foi possível registrar o veículo.")
