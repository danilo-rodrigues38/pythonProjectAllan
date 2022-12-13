alunos = {'Danilo': 7.0, 'Vinicius': 8.0, 'Jessica': 9.0, 'Ivani': 8.0, 'Eurico': 7.0}
'''
alunos = dict()
for i in range(1, 6):
    chave = str(input(f'Digite o nome do {i}º aluno: '))
    valor = float(input('Digite a nota do aluno: '))
    alunos[chave] = valor
'''
print(' ')
print(alunos)
print(' ')

soma = 0
for c in alunos.values():
    soma = soma + c
    média = soma / len(alunos)
print(f'A média da turma é {média:.2f}')
