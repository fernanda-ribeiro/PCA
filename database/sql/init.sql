CREATE TABLE Cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    cpf VARCHAR NOT NULL UNIQUE
);

CREATE TABLE Motocicleta (
    id SERIAL PRIMARY KEY,
    cod CHAR(6) NOT NULL UNIQUE,
    modelo VARCHAR NOT NULL UNIQUE,
    valor NUMERIC(20, 2) NOT NULL,
    qtd_estoque INTEGER DEFAULT 0
);

CREATE TABLE Venda (
    id SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_motocicleta INTEGER NOT NULL,
    data_venda DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_motocicleta) REFERENCES Motocicleta(id)
);