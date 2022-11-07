# Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana,
# tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem
# listas vazias, ou você tem aula?).

semana = dict()
print('CALENDÁRIO SEMANAL'.center(50))
print('*' * 50)
print(' ')
for cont in range(0, 7):
    aulas = list()
    chave = str(input('Digite o dia da semana: ')).strip().title()
    while True:
        valor = str(input(f'Digite as aulas que você tem na {chave}: ')).strip().title()
        aulas.append(valor)
        resp = str(input('\nQuer acrescentar mais alguma aula? [S/N]: ')).upper().strip()
        if resp == 'N':
            break
    semana[chave] = aulas[:]
    aulas.clear()
print('RELATÓRIO DAS ATIVIDADES SEMANAIS'.center(50))
print('*' * 50)
print(' ')
for c, v in semana.items():
    print(f'Na {c}, temos:{v}\n')
