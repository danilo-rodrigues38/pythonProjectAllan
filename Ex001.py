''' Para uma lista de 10 inteiros, elaborar um programa em Python para ordenar os elementos na lista na ordem crescente
(PROIBIDO O USO DE QUALQUER RECURSO/BIBLIOTECA/MÉTODO PRONTO DA LINGUAGEM).
O aluno deve elaborar ou utilizar um algoritmo para isso. (Bolha, Inserção, Seleção, Quick, Merge....) '''

from random import randint
from time import sleep

cont = indice = aux = 0

lista = list()

num = int(input('\nQuantos números aleatórios quer na lista: '))
for cont in range(0, num):
    lista.append(randint(0, 100))
print('\nOs números sorteados foram: ')
for cont in lista:
    print(f'{cont} ', end='')
for c in range(0, len(lista) - 1):
    for i in range(c + 1, len(lista)):
        if lista[c] > lista[i]:
            aux = lista[c]
            lista[c] = lista[i]
            lista[i] = aux
print('\n\nOs números na ordem crescente são: ')
for cont in lista:
    print(f'{cont} ', end='')
    sleep(0.3)
print('\n\nFIM DO PROGRAMA!!!')
