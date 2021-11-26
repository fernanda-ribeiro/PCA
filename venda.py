import csv
import connection_factory as cf


class Venda(cf.Connection):

    def __init__(self, **kwargs):
        cf.Connection.__init__(self)

    def insert(self, *args):
        try:
            query = f'INSERT INTO Venda (id_cliente, id_motocicleta) VALUES (%s ,%s)'
            self.executeQuery(query, tuple(args))
            self.commit()

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def insert_many(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row['id_cliente'], row['id_motocicleta'])
            print("Registros inseridos com sucesso")

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def delete(self, cod):
        try:
            sql = f'SELECT * FROM Venda WHERE id=%s'

            if self.executeQuery(sql, [cod]):
                print(f'Registro não encontrado!')
            else:
                sql = f'DELETE FROM Venda WHERE id=%s'
                self.executeQuery(sql, [cod])
                self.commit()
                print('Registro deletado com sucesso!')

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def select_all(self):
        try:
            sql = f'SELECT * FROM Venda'
            self.executeQuery(sql)
            records = self.cursor.fetchall()

            return records
        except Exception as e:
            print(f'Erro na base de dados\n{e}')

    def find_by_id(self, id):
        try:
            sql = f'SELECT * FROM Venda WHERE id = %s'
            self.executeQuery(sql, [id])
            records = self.cursor.fetchone()

            return records

        except Exception as e:
            print(f'Erro ao executar a query')