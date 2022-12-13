import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='Vrbo2404@')
cursor = conexao.cursor()
depto_id = input('Entre com o ID do Departamento: ')
cmd = 'SELECT * FROM departamentos WHERE departamento_id = ' + depto_id
cursor.execute(cmd)
resultado = cursor.fetchall()
print('Busca por departamento: ')
print('departamento_id / departamento_nome / gerente_id / local_id')
for linha in resultado:
    print(linha)
conexao.close()
