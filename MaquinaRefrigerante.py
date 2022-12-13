c5 = 0
c2 = 0
c1 = 0
c50 = 0
c25 = 0
c10 = 0
c05 = 0
c01 = 0

valor = float(input("Entre com o valor da mercadoria:"))
receb = float(input("Entre com o valor recebido:"))

troco = receb - valor

if troco == 0:
    print("Não existe troco!")
elif troco < 0:
    print("Falta(m) R$", troco * -1)
else:
    print("Troco R$", troco)
    while troco >= 5:
        troco = troco - 5
        c5 = c5 + 1
    while troco >= 2:
        troco = troco - 2
        c2 = c2 + 1
    while troco >= 1:
        troco = troco - 1
        c1 = c1 + 1
    while troco >= 0.5:
        troco = troco - 0.5
        c50 = c50 + 1
    while troco >= 0.25:
        troco = troco - 0.25
        c25 = c25 + 1
    while troco >= 0.10:
        troco = troco - 0.10
        c10 = c10 + 1
    while troco >= 0.05:
        troco = troco - 0.05
        c05 = c05 + 1
    while troco >= 0.01:
        troco = troco - 0.01
        c01 = c01 + 1

    if c5 != 0:
        print(c5, " Nota(s) de R$ 5,00")
    if c2 != 0:
        print(c2, " Nota(s) de R$ 2,00")
    if c1 != 0:
        print(c1, " Nota(s) de R$ 1,00")
    if c50 != 0:
        print(c50, " Moeda(s) de R$ 0,50")
    if c25 != 0:
        print(c25, " Moeda(s) de R$ 0,20")
    if c10 != 0:
        print(c10, " Moeda(s) de R$ 0,10")
    if c05 != 0:
        print(c05, " Moeda(s) de R$ 0,05")
    if c01 != 0:
        print(c01, " Moeda(s) de R$ 0,01")
