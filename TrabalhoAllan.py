'''
ATIVIDADE AVALIAÇÃO CONTINUADA:
- SOLUÇÃO UTILIZANDO PYTHON + CONEXÃO COM BD RELACIONAL (MYSQL)
- EM GRUPO 
- EM PAPEL 
- ELEMENTOS DO TRABALHO (MODELO BD/CÓDIGO PYTHON COMPLETO/INTERFACES (PRINTS DO CONSOLE -> IN/OUT)
- VALE 2 PONTOS 
- ENTREGA : DIA DA PROVA SEMESTRAL (IMPRETERIVELMENTE) - 29/11 (3a FEIRA)
'''

def titulo():
    print('ADMINISTRAÇÃO DE BANCO DE DADOS'.center(62))
    print('*' * 62)    


def tabelas():
    print("""
Selecione a tabela que deseja trabalhar:

1 - Cargos
2 - Departementos
3 - Funcionários
4 - Locais
5 - Países
6 - Regiões
          """)
    while True:
        tabela = int(input('Digite sua escolha: '))
        if (0 < tabela < 7):
            if tabela == 1:
                return 'cargos'
            elif tabela == 2:
                return 'departamentos'
            elif tabela == 3:
                return 'funcionarios'
            elif tabela == 4:
                return 'locais'
            elif tabela == 5:
                return 'paises'
            elif tabela == 6:
                return 'regioes'
        else:
            print('\nValor digitado incorreto!!!')
            print('Aceito somente valores entre 1 e 6.')


def escolha():
    print('\nSelecione o que quer fazer:')
    print("""
1 - Inclusão
2 - Exclusão
3 - Alteração
4 - Consulta
5 - Relatorio
          """)
    while True:
        escolha = int(input('Digite sua escolha: '))
        if (0 < escolha < 6):
            return escolha
        else:
            print('\nValor digitado incorreto!!!')
            print('Aceito somente valores entre 1 e 5.')


def inclusao():
    if (tabela == 'departamentos'):
        departamento_id = input('Entre com o Id do Departamento:')
        cmd = 'SELECT departamento_id FROM departamentos where departamento_id =' + departamento_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'cargos'):
        cargo_id = input('Entre com o Id do Cargo:')
        cmd = f'SELECT cargo_id FROM cargos where cargo_id = "{cargo_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'funcionarios'):
        funcionario_id = input('Entre com o Id do Funcionário:')
        cmd = 'SELECT funcionario_id FROM funcionarios where funcionario_id = ' + funcionario_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'locais'):
        local_id = input('Entre com o Id do Local:')
        cmd = 'SELECT local_id FROM locais where local_id = ' + local_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'paises'):
        pais_id = input('Entre com o Id do Pais:')
        cmd = f'SELECT pais_id FROM paises where pais_id = "{pais_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'regioes'):
        regiao_id = input('Entre com o Id da Região:')
        cmd = 'SELECT regiao_id FROM regioes where regiao_id = ' + regiao_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    if len(resultado) == 0:
        if ( tabela == 'departamentos'):
            print('Inclusão de Departamento:')
            depto_nome = input('Entre com o nome do departamento:')
            ger_id = input('Entre com o id do gerente:')
            loc_id = input('Entre com o id do local:')
            cmd2 = f'insert into departamentos values ({departamento_id}, "{depto_nome}", {ger_id}, {loc_id})'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Departamento {departamento_id} inserido com sucesso!')
        elif ( tabela == 'cargos'):
            print('Inclusão de Cargos:')
            cargo_desc = input('Entre com o nome do cargo:')
            min_salario = input('Entre com o valor mínimo do salário em R$:')
            max_salario = input('Entre com o valor máximo do salário em R$:')
            cmd2 = f'insert into cargos values ("{cargo_id}", "{cargo_desc}", {min_salario}, {max_salario})'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Cargo {cargo_id} inserido com sucesso!')
        elif ( tabela == 'funcionarios'):
            print('Inclusão de Funcionários:')
            pre_nome = input('Entre com o primeiro nome: ')
            sobre_nome = input('Entre com o último nome: ')
            email = input('Entre com o e-mail: ')
            fone = input('Entre com o numero do telefone: ')
            dt_admiss = input('Entre com data de admissão: ')
            cargo = input('Entre com o cargo: ')
            salario = input('Entre com o salário em R$: ')
            pc_comiss = input('Entre com a porcentagem de comissão: ')
            gerente_id = input('Entre com o ID do gerente: ')
            departamento_id = input('Entre com o ID do departamento: ')
            cmd2 = f'insert into funcionarios values ({funcionario_id}, "{pre_nome}", "{sobre_nome}", "{email}", {fone}, "{dt_admiss}", "{cargo}", {salario}, {pc_comiss}, {gerente_id}, {departamento_id})'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Funcionário {funcionario_id} inserido com sucesso!')
        if ( tabela == 'locais'):
            print('Inclusão de Locais:')
            endereco = input('Entre com o endereço: ')
            cep = input('Entre com o CEP: ')
            cidade = input('Entre com a Cidade: ')
            estado = input('Entre com o Estado: ')
            pais_id = input('Entre com a abreviação do País: ')
            cmd2 = f'insert into locais values ({local_id}, "{endereco}", "{cep}", "{cidade}", "{estado}", "{pais_id}")'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Locais {local_id} inserido com sucesso!')
        if ( tabela == 'paises'):
            print('Inclusão de Países:')
            pais_nome = input('Entre com o nome do País: ')
            regiao_id = input('Entre com região do País: ')
            cmd2 = f'insert into paises values ("{pais_id}", "{pais_nome}", {regiao_id})'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Países {pais_id} inserido com sucesso!')
        if ( tabela == 'regioes'):
            print('Inclusão de Regiôes:')
            regiao_nome = input('Entre com o nome da regiao: ')
            cmd2 = f'insert into regioes values ({regiao_id}, "{regiao_nome}")'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Regiões {regiao_id} inserido com sucesso!')
    else:
        print('Depto já existente')
    conexao.close()


def exclusao():
    if (tabela == 'departamentos'):
        departamento_id = input('Entre com o Id do Departamento:')
        cmd = 'SELECT departamento_id FROM departamentos where departamento_id =' + departamento_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'cargos'):
        cargo_id = input('Entre com o Id do Cargo:')
        cmd = f'SELECT cargo_id FROM cargos where cargo_id = "{cargo_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'funcionarios'):
        funcionario_id = input('Entre com o Id do Funcionário:')
        cmd = 'SELECT funcionario_id FROM funcionarios where funcionario_id = ' + funcionario_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'locais'):
        local_id = input('Entre com o Id do Local:')
        cmd = 'SELECT local_id FROM locais where local_id = ' + local_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'paises'):
        pais_id = input('Entre com o Id do Pais:')
        cmd = f'SELECT pais_id FROM paises where pais_id = "{pais_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'regioes'):
        regiao_id = input('Entre com o Id da Região:')
        cmd = 'SELECT regiao_id FROM regioes where regiao_id = ' + regiao_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    if len(resultado) == 0:
        print('Depto não existente. Não é possível excluir')
    else:
        if (tabela == 'departamentos'):
            print('Exclusão de Departamento:')
            cmd2 = 'delete from departamentos where departamento_id = ' + departamento_id
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Departamento {departamento_id} excluído com sucesso!')
        elif (tabela == 'cargos'):
            print('Exclusão de Cargos:')
            cmd2 = f'delete from cargos where cargo_id = "{cargo_id}"'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Cargo {cargo_id} excluído com sucesso!')
        elif (tabela == 'funcionarios'):
            print('Exclusão de Funcionários:')
            cmd2 = f'delete from funcionarios where funcionario_id = {funcionario_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Funcionário {funcionario_id} excluído com sucesso!')
        elif (tabela == 'locais'):
            print('Exclusão de Local:')
            cmd2 = f'delete from locais where local_id = {local_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Local {local_id} excluído com sucesso!')
        elif (tabela == 'paises'):
            print('Exclusão de Países:')
            cmd2 = f'delete from paises where pais_id = "{pais_id}"'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Pais {pais_id} excluído com sucesso!')
        elif (tabela == 'regioes'):
            print('Exclusão de Região:')
            cmd2 = f'delete from regioes where regiao_id = {regiao_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Região {regiao_id} excluído com sucesso!')
    conexao.close()


def alteracao():
    if (tabela == 'departamentos'):
        departamento_id = input('Entre com o Id do Departamento:')
        cmd = 'SELECT departamento_id FROM departamentos where departamento_id =' + departamento_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'cargos'):
        cargo_id = input('Entre com o Id do Cargo:')
        cmd = f'SELECT cargo_id FROM cargos where cargo_id = "{cargo_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'funcionarios'):
        funcionario_id = input('Entre com o Id do Funcionário:')
        cmd = 'SELECT funcionario_id FROM funcionarios where funcionario_id = ' + funcionario_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'locais'):
        local_id = input('Entre com o Id do Local:')
        cmd = 'SELECT local_id FROM locais where local_id = ' + local_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'paises'):
        pais_id = input('Entre com o Id do Pais:')
        cmd = f'SELECT pais_id FROM paises where pais_id = "{pais_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'regioes'):
        regiao_id = input('Entre com o Id da Região:')
        cmd = 'SELECT regiao_id FROM regioes where regiao_id = ' + regiao_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    if len(resultado) == 0:
        print('Depto não existente. Não é possível alterar')
    else:
        if ( tabela == 'departamentos'):
            print('Alteração de Departamento:')
            departamento_nome = input('Entre com o nome do depto:')
            gerente_id = input('Entre com o id do gerente:')
            local_id = input('Entre com o id do local:')
            cmd2 = f'update departamentos set departamento_nome = "{departamento_nome}", gerente_id = {gerente_id}, local_id = {local_id} where departamento_id = {departamento_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Departamento {departamento_id} alterado com sucesso!')
        elif ( tabela == 'cargos'):
            print('Alteração de Cargos:')
            cargo_desc = input('Entre com o nome do cargo:')
            min_salario = input('Entre com o valor mínimo do salário em R$:')
            max_salario = input('Entre com o valor máximo do salário em R$:')
            cmd2 = f'update cargos set cargo_desc = "{cargo_desc}", min_salario = {min_salario}, max_salario = {max_salario} where cargo_id = "{cargo_id}"'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Cargo {cargo_id} alterado com sucesso!')
        elif ( tabela == 'funcionarios'):
            print('Alteração de Funcionários:')
            pre_nome = input('Entre com o primeiro nome: ')
            sobre_nome = input('Entre com o último nome: ')
            email = input('Entre com o e-mail: ')
            fone = input('Entre com o numero do telefone: ')
            dt_admiss = input('Entre com data de admissão: ')
            cargo = input('Entre com o cargo: ')
            salario = input('Entre com o salário em R$: ')
            pc_comiss = input('Entre com a porcentagem de comissão: ')
            gerente_id = input('Entre com o ID do gerente: ')
            departamento_id = input('Entre com o ID do departamento: ')
            cmd2 = f'update funcionarios set pre_nome = "{pre_nome}", sobre_nome = "{sobre_nome}", email = "{email}", fone = {fone}, dt_admiss = "{dt_admiss}", cargo = "{cargo}", salario = {salario}, pc_comiss = {pc_comiss}, gerente_id = {gerente_id}, departamento_id = {departamento_id} where funcionario_id = {funcionario_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Funcionário {funcionario_id} alterado com sucesso!')
        if ( tabela == 'locais'):
            print('Alteração de Locais:')
            endereco = input('Entre com o endereço: ')
            cep = input('Entre com o CEP: ')
            cidade = input('Entre com a Cidade: ')
            estado = input('Entre com o Estado: ')
            pais_id = input('Entre com a abreviação do País: ')
            cmd2 = f'update locais set endereco = "{endereco}", cep = "{cep}", cidade = "{cidade}", estado = "{estado}", pais_id = "{pais_id}" where local_id = {local_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Locais {local_id} alterado com sucesso!')
        if ( tabela == 'paises'):
            print('Alteração de Países:')
            pais_nome = input('Entre com o nome do País: ')
            regiao_id = input('Entre com região do País: ')
            cmd2 = f'update paises set pais_nome = "{pais_nome}", regiao_id = {regiao_id} where pais_id = "{pais_id}"'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Países {pais_id} alterado com sucesso!')
        if ( tabela == 'regioes'):
            print('Alteração de Regiôes:')
            regiao_nome = input('Entre com o nome da regiao: ')
            cmd2 = f'update regioes set regiao_nome = "{regiao_nome}" where regiao_id = {regiao_id}'
            cursor.execute(cmd2)
            conexao.commit()
            print(f'Regiões {regiao_id} alterado com sucesso!')
    conexao.close()


def consulta():
    if (tabela == 'departamentos'):
        depto_id = input('Entre com o Id do Departamento:')
        cmd = 'SELECT * FROM departamentos where departamento_id =' + depto_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'cargos'):
        cargo_id = input('Entre com o Id do Cargo:')
        cmd = f'SELECT * FROM cargos where cargo_id = "{cargo_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'funcionarios'):
        funcionario_id = input('Entre com o Id do Funcionário:')
        cmd = 'SELECT * FROM funcionarios where funcionario_id = ' + funcionario_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'locais'):
        local_id = input('Entre com o Id do Local:')
        cmd = 'SELECT * FROM locais where local_id = ' + local_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'paises'):
        pais_id = input('Entre com o Id do Pais:')
        cmd = f'SELECT * FROM paises where pais_id = "{pais_id}"'
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    elif (tabela == 'regioes'):
        regiao_id = input('Entre com o Id da Região:')
        cmd = 'SELECT * FROM regioes where regiao_id = ' + regiao_id
        cursor.execute(cmd)
        resultado = cursor.fetchall()
    print(f'Busca por {tabela}: ')
    if (tabela == 'departamentos'):
        print('departamento_id / departamento_nome / gerente_id / local_id')
    elif (tabela == 'cargos'):
        print('cargo_id / cargo_desc / min_salario / max_salario')
    elif (tabela == 'funcionarios'):
        print('funcionario_id / pre_nome / sobre_nome / email / fone / dt_admiss / cargo / salario / pc_comiss / gerente_id / departamento_id')
    elif (tabela == 'locais'):
        print('local_id / endereco / cep / cidade / estado / pais_id')
    elif (tabela == 'paises'):
        print('pais_id / pais_nome / regiao_id')
    elif (tabela == 'regioes'):
        print('regiao_id / regiao_nome')
    for linha in resultado:
        print(linha)
    conexao.close()


def relatorio():
    cmd = f'SELECT * FROM {tabela}'
    cursor.execute(cmd)
    resultado = cursor.fetchall()
    if (tabela == 'departamentos'):
        print('departamento_id / departamento_nome / gerente_id / local_id')
    elif (tabela == 'cargos'):
        print('cargo_id / cargo_desc / min_salario / max_salario')
    elif (tabela == 'funcionarios'):
        print('funcionario_id / pre_nome / sobre_nome / email / fone / dt_admiss / cargo / salario / pc_comiss / gerente_id / departamento_id')
    elif (tabela == 'locais'):
        print('local_id / endereco / cep / cidade / estado / pais_id')
    elif (tabela == 'paises'):
        print('pais_id / pais_nome / regiao_id')
    elif (tabela == 'regioes'):
        print('regiao_id / regiao_nome')
    for linha in resultado:
        print(linha)
    conexao.close()


import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='Vrbo2404@')
cursor = conexao.cursor()
titulo()

tabela = tabelas()
print(f'\nTabela {tabela} selecionada.')
print('-' * 50)

escolha = escolha()
if escolha == 1:
    inclusao()
elif escolha == 2:
    exclusao()
elif escolha == 3:
    alteracao()
elif escolha == 4:
    consulta()
elif escolha == 5:
    relatorio()
