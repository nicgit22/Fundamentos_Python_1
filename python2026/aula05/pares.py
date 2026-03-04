def clodoaldo(x):
    resultado = x + (x+2) + (x+4) + (x+6) + (x+8)
    print(f"soma = {resultado}")



x = 1


while (x!=0):
    x = int(input("digite um numero inteiro"))

    if x == 0:
        break

    if (x%2) == 0:
        print("numero par")
        clodoaldo(x)
    else:
        print("numero impar")
        x += 1
        clodoaldo(x)
       
