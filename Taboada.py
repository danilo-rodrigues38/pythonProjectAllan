print(f'{"TABOADA":^20}')
print('~' * 20)
n = int(input('Quer ver a taboada de que número? '))
for c in range(1, 11):
    print(f'{c:2} x {n} = {n * c:2}')
print('Terminei de executar...')