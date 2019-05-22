#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Odenir Gomes
#
# Created:     15/04/2019
# Copyright:   (c) Odenir Gomes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mysql.connector


class Conexao:

    def __init__(self):
        self.conn = mysql.connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'minicursodb')

    def conectar(self):
        self.conn = mysql.connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'minicursodb')

        if self.conn.is_connected():
            print('\nConectado!')
            return self.conn.cursor()
        else:
            print('\nDesconectado!')

    def desconectar(self):

        if self.conn.is_connected():
            self.conn.close()
            return '\nDesconectado!'

    def comitar(self):
        self.conn.commit()


class CRUD:

    def __init__(self):

        self.conn = Conexao()
        self.conn.desconectar()

        self.tabela = [['alunos', 'nome, snome']]


    def cadastrar(self, indice_tabela, valores):

        cursor = self.conn.conectar()

        cursor.execute('INSERT INTO {0}({1}) VALUES ({2})' .format( self.tabela[indice_tabela][0],
                                                                    self.tabela[indice_tabela][1],
                                                                    valores))

        self.conn.comitar()
        print('Cadastro de {0} efetuado!' .format(self.tabela[indice_tabela][0]))
        self.conn.desconectar()

    def listar(self, indice_tabela):

        cursor = self.conn.conectar()

        cursor.execute('SELECT * FROM {0}' .format(self.tabela[indice_tabela][0]))
        result = cursor.fetchall()

        for r in result:
            print(r)

        self.conn.desconectar()

    def alterar(self, indice_tabela, valores, id_registro):

        cursor = self.conn.conectar()

        cursor.execute('UPDATE {0} SET {1} WHERE id = {2}' .format(self.tabela[indice_tabela][0], valores, id_registro))

        self.conn.comitar()
        self.conn.desconectar()

    def achar_registro(self, indice_tabela, id):

        cursor = self.conn.conectar()

        cursor.execute('SELECT * FROM {0} WHERE id = {1}' .format(self.tabela[indice_tabela][0], id))
        result = cursor.fetchone()

        self.conn.desconectar()

        return result

    def deletar(self, indice_tabela, id_registro):

        cursor = self.conn.conectar()


        OPCAO = input("Tem certeza que deseja deletar?\nSim<S> ou Nao<N>: ")
        if OPCAO.upper() == 'S':

            cursor.execute('DELETE FROM {0} WHERE id = {1}' .format(self.tabela[indice_tabela][0], id_registro))
            self.conn.comitar()

        self.conn.desconectar()


class Aluno:

    def __init__(self):

        self.indice = 0
        self.crud = CRUD()

    def menu(self):

        while True:

            print("\n<Menu Aluno>")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Alterar")
            print("4. Deletar")
            print("0. Sair")

            OPCAO = int(input('Entre com a opcao: '))

            if OPCAO == 1:
                self.cadastrar()

            elif OPCAO == 2:
                self.listar()

            elif OPCAO == 3:
                self.alterar()

            elif OPCAO == 4:
                self.deletar()

            elif OPCAO == 0:
                break

    def cadastrar(self):

        print('\n<Cadastrar aluno>')
        nome = input("Nome: ")
        snome = input('Snome: ')
        valores = "'{0}', '{1}'" .format(nome, snome)

        self.crud.cadastrar(self.indice, valores)

    def listar(self):

        print('\n<Listar pessoas>')
        self.crud.listar(self.indice)

    def alterar(self):

        print("/n<Alterar pessoa>")
        self.listar()

        id = input("Entre com o id: ")

        result = self.crud.achar_registro(self.indice, id)
        print("Registro selecionado -> ", result)

        nome = input("Nome: ")
        snome = input("Sobrenome: ")

        if nome == '':
            nome = result[1]

        if snome == '':
            snome = result[2]

        valores = "nome = '{0}', snome = '{1}'" .format(nome, snome)

        self.crud.alterar(self.indice, valores, id)

    def deletar(self):
        print("\n<Deletar pessoa>")

        self.listar()
        id = input("Entre com o id: ")
        result = self.crud.achar_registro(self.indice, id)
        print("Registro selecionado -> ", result)
        self.crud.deletar(self.indice, id)


def main():

    aluno = Aluno()

    while True:
        print("\n<Menu>")
        print("1. Aluno")
        print("0. Sair")

        OPCAO = int(input('Entre com a opcao: '))

        if OPCAO == 1:
            aluno.menu()

        elif OPCAO == 0:
            break

if __name__ == '__main__':
    main()
