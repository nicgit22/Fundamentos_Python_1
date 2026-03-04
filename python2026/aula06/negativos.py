lista = []

numero = int(input("quantos numeros vc quer digitar na tela"))

for i in range(numero):
    n = int(input("digite um numero"))
    lista.append(n)
for i in range(len(lista)):
    if lista[i] < 0:
        print(lista[i])
        