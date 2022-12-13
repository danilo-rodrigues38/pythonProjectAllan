import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='Vrbo2404@')
cursor = conexao.cursor()
depto_id = input('Enter com o ID do Departamento: ')
cmd = 'SELECT * FROM departamentos where departamento_id = ' + depto_id
cursor.execute(cmd)
resultado = cursor.fetchall()
if len(resultado) > 0:
    print('Busca por Departamentos: ')
    print('departamento_id/departamento_nome/gerente_id/local_id')
    for linha in resultado:
        print(linha)
else:
    print('Departamento não encontrado')
conexao.close()
