lista = []
contagem = 0
n = int(input("quantos numeros vc vai digitar"))

for i in range(n):
    numero = int(input("digite um numero"))
    lista.append(numero)
print("numeros pares: ")
for i in range(len(lista)):
    if (lista[i] % 2) == 0:
        print(lista[i])
        contagem+=1
print(f"quantidade de pares: {contagem}")
