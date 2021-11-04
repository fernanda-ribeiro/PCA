import csv
import connection_factory as cf


class Motocicleta(cf.Connection):

    def __init__(self, **kwargs):
        cf.Connection.__init__(self)

    def insert(self, *args):
        try:
            query = f'INSERT INTO Motocicleta (cod, modelo, valor, qtd_estoque) VALUES (%s ,%s, %s, %s)'
            self.executeQuery(query, tuple(args))
            self.commit()

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def insert_many(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row['cod'], row['modelo'], row['valor'], row['qtd_estoque'])
            print("Registros inseridos com sucesso")

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def delete(self, cod):
        try:
            sql = f'SELECT * FROM Motocicleta WHERE cod=%s'

            if self.executeQuery(sql, [cod]):
                print(f'Registro não encontrado!')
            else:
                sql = f'DELETE FROM Motocicleta WHERE cod=%s'
                self.executeQuery(sql, [cod])
                self.commit()
                print('Registro deletado com sucesso!')

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')
