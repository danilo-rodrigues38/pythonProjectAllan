# Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave.
# E, como valor, outro dicionário contendo o protagonista e o ano em que o filme foi lançado.
# Preencha 5 filmes.

filme = dict()
protagAno = dict()

print('CADASTRO DE FILMES'.center(60))
print('*' * 60, '\n')
for cont in range(0, 5):
    titulo = str(input('Digite o nome do filme: ')).strip().title()
    nome = str(input('Digite o nome do protagonista do filme: ')).strip().title()
    ano = int(input('Digite o ano de lançamento do filme: '))
    protagAno[nome] = ano
    filme[titulo] = protagAno
for c, v in filme.items():
    print(f'O filme {c}, tem como protagonista e ano de lançamento: {v}')
