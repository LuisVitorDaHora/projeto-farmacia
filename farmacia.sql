CREATE DATABASE farmacia;
USE farmacia;

/* Lógico_1: */

CREATE TABLE tbl_produtos (
    id_produtos INT AUTO_INCREMENT PRIMARY KEY,
    nome_produtos VARCHAR(100) NOT NULL,
    preco_produtos DECIMAL(10, 2) NOT NULL,
    descricao_produtos VARCHAR(500),
    dt_validade_produtos DATETIME NOT NULL
);

CREATE TABLE tbl_funcionarios (
    id_funcionarios INT AUTO_INCREMENT PRIMARY KEY,
    nome_funcionarios VARCHAR(100) NOT NULL,
    cpf_funcionarios VARCHAR(14) NOT NULL,
    cargo_funcionarios VARCHAR(100) NOT NULL
);

CREATE TABLE tbl_entrada_estoque (
    id_entrada INT AUTO_INCREMENT PRIMARY KEY,
    data_entrada DATE NOT NULL,
    quantidade_entrada INT
);

CREATE TABLE tbl_saida_estoque (
	id_saida INT AUTO_INCREMENT PRIMARY KEY,
    data_saida DATE NOT NULL,
    quantidade_saida INT
);

CREATE TABLE tbl_fornecedor (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(100) NOT NULL,
    contato_fornecedor VARCHAR(100) NOT NULL
);

CREATE TABLE tbl_estoque (
    id_estoque INT AUTO_INCREMENT PRIMARY KEY,
    qtde_estoque INT,
    lote_estoque VARCHAR(100) NOT NULL
);

CREATE TABLE func_forn (
    fk_tbl_funcionarios_id_funcionarios INT,
    fk_tbl_fornecedor_id_fornecedor INT
);

CREATE TABLE func_pro (
    fk_tbl_funcionarios_id_funcionarios INT,
    fk_tbl_produtos_id_produtos INT
);

CREATE TABLE esto_said (
    fk_tbl_estoque_id_estoque INT,
    fk_tbl_saida_estoque_id_saida INT
);

CREATE TABLE esto_entr (
    fk_tbl_entrada_estoque_id_entrada INT,
    fk_tbl_estoque_id_estoque INT
);

CREATE TABLE prod_entr (
    fk_tbl_produtos_id_produtos INT,
    fk_tbl_entrada_estoque_id_entrada INT
);

CREATE TABLE forn_prod (
    fk_tbl_fornecedor_id_fornecedor INT,
    fk_tbl_produtos_id_produtos INT
);

CREATE TABLE prod_esto (
    fk_tbl_produtos_id_produtos INT,
    fk_tbl_estoque_id_estoque INT
);

CREATE TABLE prod_said (
    fk_tbl_produtos_id_produtos INT,
    fk_tbl_saida_estoque_id_saida INT
);
 
ALTER TABLE func_forn ADD CONSTRAINT FK_func_forn_1
    FOREIGN KEY (fk_tbl_funcionarios_id_funcionarios)
    REFERENCES tbl_funcionarios (id_funcionarios)
    ON DELETE RESTRICT;
 
ALTER TABLE func_forn ADD CONSTRAINT FK_func_forn_2
    FOREIGN KEY (fk_tbl_fornecedor_id_fornecedor)
    REFERENCES tbl_fornecedor (id_fornecedor)
    ON DELETE RESTRICT;
 
ALTER TABLE func_pro ADD CONSTRAINT FK_func_pro_1
    FOREIGN KEY (fk_tbl_funcionarios_id_funcionarios)
    REFERENCES tbl_funcionarios (id_funcionarios)
    ON DELETE RESTRICT;
 
ALTER TABLE func_pro ADD CONSTRAINT FK_func_pro_2
    FOREIGN KEY (fk_tbl_produtos_id_produtos)
    REFERENCES tbl_produtos (id_produtos)
    ON DELETE RESTRICT;
 
ALTER TABLE esto_said ADD CONSTRAINT FK_esto_said_1
    FOREIGN KEY (fk_tbl_estoque_id_estoque)
    REFERENCES tbl_estoque (id_estoque)
    ON DELETE RESTRICT;
 
ALTER TABLE esto_said ADD CONSTRAINT FK_esto_said_2
    FOREIGN KEY (fk_tbl_saida_estoque_id_saida)
    REFERENCES tbl_saida_estoque (id_saida)
    ON DELETE RESTRICT;
 
ALTER TABLE esto_entr ADD CONSTRAINT FK_esto_entr_1
    FOREIGN KEY (fk_tbl_entrada_estoque_id_entrada)
    REFERENCES tbl_entrada_estoque (id_entrada)
    ON DELETE RESTRICT;
 
ALTER TABLE esto_entr ADD CONSTRAINT FK_esto_entr_2
    FOREIGN KEY (fk_tbl_estoque_id_estoque)
    REFERENCES tbl_estoque (id_estoque)
    ON DELETE SET NULL;
 
ALTER TABLE prod_entr ADD CONSTRAINT FK_prod_entr_1
    FOREIGN KEY (fk_tbl_produtos_id_produtos)
    REFERENCES tbl_produtos (id_produtos)
    ON DELETE RESTRICT;
 
ALTER TABLE prod_entr ADD CONSTRAINT FK_prod_entr_2
    FOREIGN KEY (fk_tbl_entrada_estoque_id_entrada)
    REFERENCES tbl_entrada_estoque (id_entrada)
    ON DELETE RESTRICT;
 
ALTER TABLE forn_prod ADD CONSTRAINT FK_forn_prod_1
    FOREIGN KEY (fk_tbl_fornecedor_id_fornecedor)
    REFERENCES tbl_fornecedor (id_fornecedor)
    ON DELETE RESTRICT;
 
ALTER TABLE forn_prod ADD CONSTRAINT FK_forn_prod_2
    FOREIGN KEY (fk_tbl_produtos_id_produtos)
    REFERENCES tbl_produtos (id_produtos)
    ON DELETE RESTRICT;
 
ALTER TABLE prod_esto ADD CONSTRAINT FK_prod_esto_1
    FOREIGN KEY (fk_tbl_produtos_id_produtos)
    REFERENCES tbl_produtos (id_produtos)
    ON DELETE RESTRICT;
 
ALTER TABLE prod_esto ADD CONSTRAINT FK_prod_esto_2
    FOREIGN KEY (fk_tbl_estoque_id_estoque)
    REFERENCES tbl_estoque (id_estoque)
    ON DELETE SET NULL;
 
ALTER TABLE prod_said ADD CONSTRAINT FK_prod_said_1
    FOREIGN KEY (fk_tbl_produtos_id_produtos)
    REFERENCES tbl_produtos (id_produtos)
    ON DELETE SET NULL;
 
ALTER TABLE prod_said ADD CONSTRAINT FK_prod_said_2
    FOREIGN KEY (fk_tbl_saida_estoque_id_saida)
    REFERENCES tbl_saida_estoque (id_saida)
    ON DELETE SET NULL;