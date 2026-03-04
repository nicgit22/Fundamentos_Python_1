codiogo = input("codiog do produto comprado")
quantidade = int(input("quantidade comprada"))
produtos = {"1":5.00, "2": 3.50, "3": 4.80, "4":8.90, "5": 7.32}
valor = quantidade * produtos[codiogo]
print("valor a pagar é de ",valor)
