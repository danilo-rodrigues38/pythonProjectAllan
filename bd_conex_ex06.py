import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='pl3417320')
cursor = conexao.cursor()
depto_id = input('Entre com o Id do Departamento:')
cmd = 'SELECT departamento_id FROM departamentos where departamento_id ='+depto_id
cursor.execute(cmd)
resultado = cursor.fetchall()
if len(resultado) == 0:
     print('Depto não existente. Não é possível alterar')
else:
     print('Alteração de Departamento:')
     depto_nome = input('Entre com o NOVO nome do depto:')
     ger_id = input('Entre com o NOVO id do gerente:')
     loc_id = input('Entre com o NOVO id do local:')
     cmd2 = 'update departamentos set departamento_nome = "'+depto_nome+'", gerente_id = '+ger_id+', local_id = '+loc_id+' where departamento_id = '+ depto_id
     #print(cmd2)
     cursor.execute(cmd2)
     conexao.commit()
     print('Depto '+depto_id+' alterado com sucesso!')
conexao.close()