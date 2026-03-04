RESP1 = "quantos casos vai digitar? " #variavel constante

try:
    #entrada de dados
    n = int(input("quantos casos vai digitar? "))

    for i in range(n):#variavel n define o valor do loop
        x = float(input("digite o numerador "))
        y = float(input("digite o denominador "))
        if (y == 0):
            print("divisão inpossivel")
        else:
            resultado = x / y
            print(f"divisão = {resultado:.2f}")
except:
    print("digite valores validos")