import telas
from motocicleta import Motocicleta

def main():
    exit = False

    print(f'''
    888888b.                                        d8b               888          
    888  "88b                                       Y8P               888          
    888  .88P                                                         888          
    8888888K.   .d88b.  88888b.d88b.       888  888 888 88888b.   .d88888  .d88b.  
    888  "Y88b d8P  Y8b 888 "888 "88b      888  888 888 888 "88b d88" 888 d88""88b 
    888    888 88888888 888  888  888      Y88  88P 888 888  888 888  888 888  888 
    888   d88P Y8b.     888  888  888       Y8bd8P  888 888  888 Y88b 888 Y88..88P 
    8888888P"   "Y8888  888  888  888        Y88P   888 888  888  "Y88888  "Y88P"  
                                                                                                                                                             
''')

    while not exit:
        print(f'''
    SELECIONE O NÚMERO CORRESPONDENTE A OPÇÃO DESEJADA:
    
    1 -  Cadastrar Cliente
    2 -  Registrar Veículo
    3 -  Deletar um registro
    4 -  Sair 
''')
        opt = int(input(">> ").strip())
        exit = opt == 4

        if opt == 1 or opt == 2:
            telas.cadastrar(opt)
        
        if opt == 3:
            telas.deletar()


if __name__ == '__main__':
    # db = Motocicleta()
    # db.insert_many('./database/data/motocicleta.csv')
    main()