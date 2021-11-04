import psycopg2 as db


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "admin",
                "password": "admin",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "dealership"
            }
        }


class Connection(Config):
    def __init__(self):
        Config.__init__(self)

        try:
            self.conn = db.connect(**self.config.get("postgres"))
            self.cur = self.conn.cursor()

        except Exception as e:
            print(f'''Erro ao se conectar ao banco de dados\n{e}''')
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.cursor.close()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchAll(self):
        return self.cursor.fetchAll()

    def executeQuery(self, query, params=()):
        self.cursor.execute(query, params)

    def query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchAll()
