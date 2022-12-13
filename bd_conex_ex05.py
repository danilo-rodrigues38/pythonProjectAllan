import pymysql
conexao = pymysql.connect(db='rh', user='aluno', passwd='toor')
cursor = conexao.cursor()
depto_id = input('Entre com o Id do Departamento:')
cmd = 'SELECT departamento_id FROM departamentos where departamento_id ='+depto_id
cursor.execute(cmd)
resultado = cursor.fetchall()
if len(resultado) == 0:
     print('Depto não existente. Não é possível excluir')
else:
     print('Exclusão de Departamento:')
     cmd2 = 'delete from departamentos where departamento_id = '+ depto_id
     #print(cmd2)
     cursor.execute(cmd2)
     conexao.commit()
     print('Depto '+depto_id+' excluído com sucesso!')
conexao.close()