import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='Vrbo2404@')
cursor = conexao.cursor()
cmd = 'SELECT * FROM departamentos'
cursor.execute(cmd)
resultado = cursor.fetchall()
print('departamento_id / departamento_nome / gerente_id / local_id')
for linha in resultado:
    print(linha)
conexao.close()
