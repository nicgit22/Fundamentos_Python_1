try:
    import math as mt
    #biblioteca math renomeada por mt


    def delta(a, b, c):
        delta = mt.pow(b,2) - 4 * a * c
        return delta
    #função p/ calcular o valor de delta

    def raizes(delta, a, b):
        raiz1 = (- b + mt.sqrt(delta)) / (2 * a)
        raiz2 = (- b - mt.sqrt(delta)) / (2 * a)
        saida = f" Raiz 1 = {raiz1:.2f}\n\traiz 2 = {raiz2:.2f}"
        return saida

        #mt.square faz a raiz de delta
        #calcular raizes

    #entrada de dados
    print("--aplicativo para calcular as raizes de uma equação do 2 grau--")
    a = float(input("digite o valor de a"))
    b= float(input("digite o valor de b"))
    c = float(input("digite o valor de c"))
    print(f"Equação -> {a}x² + {b}x {c} = 0")

    #processamento de daods
    delta1 = delta(a,b,c)


    
    if delta1 < 0:
        print("raizes impossiveis")
    else:
        dados = raizes(delta1, a, b)
        print(f"as raizes da equação de 2 graus são:\n\t{dados}")

except ValueError:
    print("digite um valor valido ")
except ZeroDivisionError:
    print("digite um valor A diferente de zero")
