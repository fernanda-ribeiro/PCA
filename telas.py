from venda import Venda
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

def vender():
    print(f'''\n************ REGISTRAR NOVA VENDA ************''')
    comprador = input("CPF DO CLIENTE >> ")
    cliente = Cliente()
    comprador = cliente.find_by_cpf(comprador)

    veiculo = input("CÓDIGO DO VEÍCULO >> ")
    moto = Motocicleta()
    veiculo = moto.find_by_code(veiculo)

    try:
        venda = Venda()
        venda.insert(comprador[0], veiculo[0])
        print("\nVenda realizada com sucesso!")

    except Exception as  e:
        print("\nNão foi possível registrar o veículo.")

def listar_vendas():
    vendas = Venda()
    registros = vendas.select_all()

    print(f'COD\t CLIENTE\t VEÍCULO\t DATA\n')

    for datas in registros:
        cliente = Cliente().find_by_id(datas[1])
        veiculo = Motocicleta().find_by_id(datas[2])

        print(f'{datas[0]}\t {cliente[4]}\t  {veiculo[1]}\t {datas[3]}')

    input("\nPress ENTER to continue")

def consultar_venda():
    print(f'''\n************ CONSULTAR REGISTRO DE VENDA ************\n''')
    opt = input("CÓDIGO DA VENDA >> ")

    try:
        venda = Venda().find_by_id(int(opt))
        cliente = Cliente().find_by_id(venda[1])
        moto = Motocicleta().find_by_id(venda[2])

        print(f'''\n INFO VENDA CÓDIGO {venda[0]}\n
        CLIENTE:
        
        NOME:     {cliente[1]}
        TELEFONE: {cliente[2]}
        EMAIL:    {cliente[3]}
        CPF:      {cliente[4]}
        
        VEICULO:
        
        CÓDIGO: {moto[1]}
        MODELO: {moto[2]}
        VALOR:  {moto[3]}
        
        VENDA REALIZADA EM: {venda[3]}        

''')
        input("Press ENTER to continue")

    except Exception as e:
        print(f'\nCÓDIGO NÃO ENCONTRADO')