import csv
import connection_factory as cf


class Cliente(cf.Connection):

    def __init__(self, **kwargs):
        cf.Connection.__init__(self)

    def insert(self, *args):
        try:
            query = f'INSERT INTO Cliente (nome, telefone, email, cpf) VALUES (%s, %s, %s, %s)'
            self.executeQuery(query, tuple(args))
            self.commit()

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def insert_many(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row['nome'], row['telefone'], row['email'], row['cpf'])
            print("Registros inseridos com sucesso")

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def delete(self, id):
        try:
            sql = f'SELECT * FROM Cliente WHERE id=%s'

            if self.executeQuery(sql, [id]):
                print(f'Registro não encontrado!')
            else:
                sql = f'DELETE FROM Cliente WHERE id=%s'
                self.executeQuery(sql, [id])
                self.commit()
                print('Registro deletado com sucesso!')

        except Exception as e:
            print(f'Erro ao inserir os dados\n{e}')

    def find_by_cpf(self, cpf):
        try:
            sql = f'SELECT * FROM Cliente WHERE cpf = %s'
            self.executeQuery(sql, [cpf])
            records = self.cursor.fetchone()

            return records

        except Exception as e:
            print(f'Erro ao executar a query')

    def find_by_id(self, id):
        try:
            sql = f'SELECT * FROM Cliente WHERE id = %s'
            self.executeQuery(sql, [id])
            records = self.cursor.fetchone()

            return records

        except Exception as e:
            print(f'Erro ao executar a query')
