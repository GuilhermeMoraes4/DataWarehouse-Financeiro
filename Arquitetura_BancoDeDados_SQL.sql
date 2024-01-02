CREATE DATABASE FinanceDB; -- Criação do banco de dados.
USE FinanceDB;

-- Criação da Tabela Associados
CREATE TABLE Associados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    sobrenome VARCHAR(100),
    idade INT,
    email VARCHAR(100)
);

-- Criação da Tabela Contas e seus relacionamentos
CREATE TABLE Contas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_conta VARCHAR(50),
    data_criacao TIMESTAMP,
    id_associado INT,
    FOREIGN KEY (id_associado) REFERENCES Associados (id)
);

-- Criaçao da Tabela Cartões e seus relacionamentos
CREATE TABLE Cartoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    num_cartao BIGINT,
    nom_impresso VARCHAR(100),
    id_conta INT,
    id_associado INT,
    FOREIGN KEY (id_conta) REFERENCES Contas (id),
    FOREIGN KEY (id_associado) REFERENCES Associados (id)
);

-- Criação da Tabela Movimentações e seus relacionamentos
CREATE TABLE Movimentacoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vlr_transacao DECIMAL(10, 2),
    des_transacao VARCHAR(255),
    data_movimento TIMESTAMP,
    id_cartao INT,
    FOREIGN KEY (id_cartao) REFERENCES Cartoes (id)
);
