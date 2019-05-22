

#CRIA UM BANCO DE DADOS
CREATE DATABASE testDB;

#USAR BANCO DE DADOS
USE testDB;

#CRIA UMA TABELA
CREATE TABLE alunos (matricula int auto_increment, nome varchar(20), snome varchar(20), primary key(matricula));

#APAGAR TABELA
DROP TABLE alunos;

#ENTRADA DE DADOS
INSERT INTO alunos values (default, 'João', 'Gomes'), (default, 'Jorge', 'Silva');

#SAIDA DE DADOS
SELECT * from alunos;

#DELETAR DADOS
delete from alunos where matricula = '1';

#ALTERAR DADOS
UPDATE alunos SET nome = 'Jorge' where matricula = '1';

