import sqlite3

from sqlite3 import Error

lista =[]

class Informacoes:
    def __init__(self, nome, Cep, email, telefone, nascimento):
        self.nome_completo = nome
        self.cep = Cep
        self.email = email
        self.numero_celular = telefone
        self.data_nascimento = nascimento

    def get_nome_completo(self):
        return self.nome_completo

    def set_nome_completo(self, valor):
        self.nome_completo = valor

    def get_cep(self):
        return self.cep

    def set_cep(self, valor):
        self.cep = valor

    def get_email(self):
        return self.email

    def set_email(self, valor):
        self.email = valor

    def get_telefone(self):
        return self.numero_celular

    def set_telefone(self, valor):
        self.numero_celular = valor

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, valor):
        self.data_nascimento = valor

    def retorna_dados(self):
        s = 'Nome: ' + self.nome_completo + '' + \
            '\nCEP: ' + str(self.cep) + '' + \
            '\nEmail: ' + str(self.email) + '' + \
            '\nTelefone; ' + str(self.numero_celular) + '' + \
            '\nData de Nascimento: ' + str(self.data_nascimento)
        return s


class Funcionario(Informacoes):
    def __init__(self, nome, Cep, email, telefone, nascimento, salario, carga_trabalho_semanal):
        super().__init__(nome, Cep, email, telefone, nascimento)
        self.salario = salario
        self.hora = carga_trabalho_semanal

    def bonifica_funcionario(self):
        return self.salario * 1.10


def insert_dados():
    sql = f'''insert into {tabela}(nome_medicamento, fabricante, preco, data_validade, dosagem) values(?, ?, ?, ?, ?)'''
    nome_medicamento = input('Digite o nome do medicamento: ')
    fabricante = input('Digite quem é o fabricante: ')
    preco = float(input('Insira o preço do remédio: '))
    data_validade = input('Coloque a data de validade: ')
    dosagem = float(input('Informe a dosagem: '))
    try:
        cur.execute(sql, (nome_medicamento, fabricante, preco, data_validade, dosagem))
        conexao.commit()  # gravar na memória
        print('one record added sucessfully')
    except Error as e:
        print('Mensagem de erro no insert_dados')
        print(e)
        conexao.rollback()


def seleciona_dados():
    sql1 = f'SELECT * from {tabela}'
    try:
        cur.execute(sql1)
        # direcao.execute(sql,)   # vai mostrar os números dentro de uma váriavel - registros
        cadastro = cur.fetchall()
        print('Consultando todos')
        for cadastro in cadastro:  # mostrar na vertical
            print(cadastro)
            print('Total de registros: ', len(cadastro))
    except Error as e:
        print('Mensagem de erro no select_dados')
        print(e)


def atualizar_dados():
    seleciona_dados()
    opcao1 = input('Digite o que você quer mudar, '
                   'escreva exatamente como as opções a seguir:'
                   '\nnome_medicamento ou'
                   '\nfabricante ou'
                   '\npreco ou'
                   '\ndata_validade ou'
                   '\ndosagem: ')
    opcao2 = input('Digite o que você você irá informar pra fazer a mudança , '
                   'escreva exatamente como as opções a seguir:'
                   '\nnome_medicamento ou'
                   '\nfabricante ou'
                   '\npreco ou'
                   '\ndata_validade ou'
                   '\ndosagem: ')
    sql2 = f"update {tabela} set {opcao1}=? where {opcao2}=?"  # "update tb_livro set autor='Ana' where titulo='oi'"

    if opcao1 == 'nome_medicamento' and opcao2 == 'fabricante':
        novo_medicamento = input('Nome do remédio: ')
        nome_fabricante = input('Fabricante: ')
        try:
            cur.execute(sql2, (novo_medicamento, nome_fabricante))
            v = cur.rowcount  # verifica se o comando afetou quantas linhas
            if v > 0:
                print('Registro cadastrado')
            else:
                print('Registro não cadastrado')
            conexao.commit()
        except Error as e:
            print('Except no def atualizar_dados')
            print(e)
            conexao.rollback()  # desfazer comandos

    elif opcao1 == 'fabricante' and opcao2 == 'preco':
        novo_fabricante = input('Novo Fabricante:')
        preco = float(input('Preço: '))
        try:
            cur.execute(sql2, (novo_fabricante, preco))
            v = cur.rowcount  # verifica se o comando afetou quantas linhas
            if v > 0:
                print('Registro cadastrado')
            else:
                print('Registro não cadastrado')
            conexao.commit()
        except Error as e:
            print('Except no def atualizar_dados')
            print(e)
            conexao.rollback()  # desfazer comandos


def deletar_dado():
    seleciona_dados()
    escolha = input('Digite de onde você quer deletar, '
                    'escreva exatamente como as opções a seguir:'
                    '\nnome_medicamento ou'
                    '\nfabricante ou'
                    '\npreco ou'
                    '\ndata_validade ou'
                    '\ndosagem: ')

    while escolha != 'nome_medicamento' and escolha != 'fabricante' and escolha != 'preco' and escolha != 'data_validade' and escolha != 'dosagem':
        print('\nOpção inválida, tente novamente\n')
        escolha = input('Digite de onde você quer deletar, '
                        'escreva exatamente como as opções a seguir:'
                        '\nnome_medicamento ou'
                        '\nfabricante ou'
                        '\npreco ou'
                        '\ndata_validade ou'
                        '\ndosagem: ')

    sql3 = f"delete from {tabela} where {escolha}=?"

    if escolha == 'nome_medicamento':
        nome_medicamento = input('Insira o nome do remédio que será deletado: ')
        try:
            cur.execute(sql3, (nome_medicamento,))
            va = cur.rowcount
            if va > 0:
                print('Registro deletado')
            else:
                print('Registro não deletado')
            conexao.commit()
        except Error as e:
            print('Except no def deletar_dado')
            print(e)
            conexao.rollback()

    elif escolha == 'fabricante':
        nome_fabricante = input('Insira o nome do fabricante que será deletado: ')
        try:
            cur.execute(sql3, (nome_fabricante,))
            va = cur.rowcount
            if va > 0:
                print('Registro deletado')
            else:
                print('Registro não deletado')
            conexao.commit()
        except Error as e:
            print('Except no def deletar_dado')
            print(e)
            conexao.rollback()

    elif escolha == 'dosagem':
        qt_dosagem = float(input('Insira a dosagem (quantidade) que será deletado: '))
        try:
            cur.execute(sql3, (qt_dosagem,))
            va = cur.rowcount
            if va > 0:
                print('Registro deletado')
            else:
                print('Registro não deletado')
            conexao.commit()
        except Error as e:
            print('Except no def deletar_dado')
            print(e)
            conexao.rollback()


if __name__ == '__main__':
    F1 = Funcionario('Paulo', '71987-566', 'umeao@gmail.com', '99867-5541', '01/12/1999', 900, '40 horas')
    print(F1.retorna_dados())
    print(f'Salário antes da bonificação: {F1.salario}')
    print(f'Salário após a bonificação de 10%: {F1.bonifica_funcionario()}')
    print(f'Carga de trabalho semanal de {F1.hora}')

    database = 'farmacia.db'
    conexao = sqlite3.connect(database)
    tabela = input('Digite o nome da tabela para ser criada - na nomenclatura tb_nome: ')

    try:
        cur = conexao.cursor()  # percorrer todos os registros de dados
        cur.execute(f'create table if not exists {tabela}('
                    f'identificador integer primary key autoincrement,'
                    f'nome_medicamento text,'
                    f'fabricante text not null,'
                    f'preco float,'
                    f'data_validade text,'
                    f'dosagem float)')
        conexao.commit()
    except Error as e:
        print('Erro ao criar tabela')
        print(e)
        conexao.rollback()
        cur.close()
        conexao.close()
        exit(0)

    escolha = int(input('Digite [1] para usar lista ou [2] para sql: '))
while True:

    while escolha != 1 and escolha != 2:
        print('\nOpção inválida, tente novamente\n')
        escolha = int(input('Digite [1] para usar lista ou [2] para sql: '))

    if escolha == 1:
        x = int(input('Digite:'
                      '\n[1] para adicionar novo produto'
                      '\n[2] para ver os produtos cadastrados'
                      '\n[3] para deletar algum produto'
                      '\n[4] para atualizar produto'
                      '\n[5] para deletar tabela'
                      '\n[6] para sair: '))

        while x != 1 and x != 2 and x != 3 and x != 4 and x != 5:
            print('\nOpção inválida, tente novamente\n')
            x = int(input('Digite:'
                          '\n[1] para adicionar novo produto'
                          '\n[2] para ver os produtos cadastrados'
                          '\n[3] para deletar algum produto'
                          '\n[4] para atualizar produto'
                          '\n[5] para deletar tabela'
                          '\n[6] para sair: '))

        if x == 1:
            print('\nVocê escolheu adicionar um novo produto\n'
                  'Digite [1] para escolher a posição\nPara sair tecle [-1]')
            choise = int(input('Qual a sua escolha?'))

            if choise == 1:
                position = int(input('Posição:\nOU [-1] para sair\n'))
                while position != -1:
                    nome_produto = input('Qual o nome do produto?')
                    lista.insert(position, nome_produto)
                    position = int(input('Posição:\nou [-1] para sair'))
                print(lista)

            elif choise == -1:
                pass

            else:
                print('Tente novamente')

        elif x == 2:
            print('Você escolheu visualizar os cadastros existentes')
            if lista:
                for indice, v in enumerate(lista):
                    print(indice, '...........', v)

            print(lista)



        elif x == 3:
            print('Você escolheu deletar um produto')
            if lista:
                if lista:
                    for indice, v in enumerate(lista):
                        print(indice, '...........', v)
                print('\n[1] para posição\n[2] para o nome do produto\n[-1] para sair')
                choise = int(input('Qual sua escolha?'))

                if choise == 1:
                    position = int(input('Qual posição deseja excluir?'))
                    size = len(lista)
                    if position <= size - 1:
                        lista.pop(position)
                    else:
                        print('A posição', position, 'não existe na lista')

                elif choise == 2:
                    nome_produto = input('Qual o nome do produto?')
                    if nome_produto in lista:
                        lista.remove(nome_produto)
                    else:
                        print('O nome', nome_produto, 'não existe na lista')

                elif choise == -1:
                    pass

                else:
                    print('Opção inválida.'
                          '\nTente novamente')

        if x == 4:
            print(lista)
            print('Você escolheu atualizar um produto'
                  '\n[1] para Posição'
                  '\n[2] para Nome'
                  '\n[-1] para Sair')
            choisee = int(input('Qual a sua escolha?'))

            if choisee == 1:
                positionn = int(input('Qual a posição?'))
                new_product = input('Qual o nome do novo produto?')
                try:
                    lista[positionn] = new_product
                except IndexError as e:
                    print('Erro IndexError: ', e)
                except Exception as e:
                    print('Errp Exception: ', e)

            elif choisee == 2:
                old_product = input('Qual o nome do produto que vai ser substituido?')
                if old_product in lista:
                    a = lista.index(old_product)
                    novo_produto = input('Digite o novo produto: ')
                    lista[a] = novo_produto
                else:
                    print(old_product, 'não está na lista')

            elif choisee == -1:
                pass

            else:
                print('Opção inválida, tente novamente')
    if escolha == 2:
        x = int(input('Digite:'
                      '\n[1] para adicionar novo produto'
                      '\n[2] para ver os produtos cadastrados'
                      '\n[3] para deletar algum produto'
                      '\n[4] para atualizar produto'
                      '\n[5] para deletar tabela'
                      '\n[6] para sair: '))

        while x != 1 and x != 2 and x != 3 and x != 4 and x != 5:
            print('\nOpção inválida, tente novamente\n')
            x = int(input('Digite:'
                          '\n[1] para adicionar novo produto'
                          '\n[2] para ver os produtos cadastrados'
                          '\n[3] para deletar algum produto'
                          '\n[4] para atualizar produto'
                          '\n[5] para deletar tabela'
                          '\n[6] para sair: '))
        if x == 1:
            insert_dados()
        elif x == 2:
            seleciona_dados()
        elif x == 3:
            deletar_dado()
        elif x == 4:
            atualizar_dados()
        elif x == 5:
            cur.execute(f'drop table {tabela}')
            break
        else:
            break
