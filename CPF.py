print('\n')
print("Verificador de CPF".center(40))
print('~' * 40)
print('\nInforme o CPF sem pontos e traços.\n')
cpf = str(input('Digite o número do CPF: ')).strip()
c = i = res1 = res2 = verificador1 = verificador2 = 0

if len(cpf) == 11:
    for cont in range(10, 1, -1):
        mult = (int(cpf[c]) * cont)
        res1 += mult
        c += 1
    verificador1 = (res1 * 10) % 11
    for cont in range(11, 1, -1):
        mult = (int(cpf[i]) * cont)
        res2 += mult
        i += 1
    verificador2 = (res2 * 10) % 11
    if (verificador1 != int(cpf[-2])) and (verificador2 != int(cpf[-1])):
        print('\nCPF digitado é inválido!!!\n')
    else:
        print('\nO CPF é válido!!!\n')
else:
    print('\nCPF digitado é inválido!!!\n')
