cand1 = cand2 = cand3 = nulo = branco = total = 0


while True:
    print(F'{"ELEIÇÕES 2022":^30}')
    print('=' * 30)
    print("""
    1 - Eymael
    2 - Levy Fidelix
    3 - Cabo Daciolo
    4 - Voto em Branco
    5 - Voto Nulo
    """)
    escolha = int(input(f'{"Escolha um candidato:":} '))
    total += 1
    if escolha == 1:
        cand1 += 1
    elif escolha == 2:
        cand2 += 1
    elif escolha == 3:
        cand3 += 1
    elif escolha == 4:
        branco += 1
    else:
        nulo += 1
    resp = str(input('Quer continuar: [S/N] ')).strip().lower()
    if resp in 'Nn':
        break
print('\n')
print(f'O total de votos foi: \033[0;34m{total}\033[m')

print(f'O candidato Eymael teve \033[0;34m{cand1}\033[m votos, correspondente'
      f' a \033[0;34m{((cand1 / total) * 100):.1f}%\033[m dos votos vádilos.')

print(f'O candidato Levy Fedelix teve \033[0;34m{cand2}\033[m votos, correspondente'
      f' a \033[0;34m{((cand2 / total) * 100):.1f}%\033[m dos votos vádilos.')

print(f'O candidato Cabo Daciolo teve \033[0;34m{cand3}\033[m votos, correspondente'
      f' a \033[0;34m{((cand3 / total) * 100):.1f}%\033[m dos votos vádilos.')

print(f'Votos nulos foram \033[0;34m{nulo}\033[m votos, correspondente'
      f' a \033[0;34m{((nulo / total) * 100):.1f}%\033[m dos votos vádilos.')

print(f'Votos brancos foram \033[0;34m{branco}\033[m votos, correspondente'
      f' a \033[0;34m{((branco / total) * 100):.1f}%\033[m dos votos vádilos.')

