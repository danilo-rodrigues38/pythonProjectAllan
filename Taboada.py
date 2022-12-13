print(' ')
print(f'{"TABOADA":^35}')
print('~' * 35)
n = int(input('\nQuer ver a taboada de que número? '))
print(' ')
for c in range(1, 11):
    print(f'{c:2} x {n} = {n * c:2}')
print('\nTerminei de executar...\n')