import pymysql
conexao = pymysql.connect(db='rh', user='root', passwd='Vrbo2404@')
cursor = conexao.cursor()
depto_id = input('Entre com o Id do Departamento:')
cmd = 'SELECT departamento_id FROM departamentos where departamento_id =' + depto_id
cursor.execute(cmd)
resultado = cursor.fetchall()
if len(resultado) == 0:
     print('Inclusão de Departamento:')
     depto_nome = input('Entre com o nome do Departamento:')
     ger_id = input('Entre com o id do gerente:')
     loc_id = input('Entre com o local id do Departamento:')
     cmd2 = 'insert into departamentos values ('+ depto_id +',"'+depto_nome+'",'+ger_id+','+loc_id+')'
     #print(cmd2)
     cursor.execute(cmd2)
     conexao.commit()
     print('Depto '+depto_id+' inserido com sucesso!')
else:
     print('Depto já existente')
conexao.close()