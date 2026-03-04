a = float(input("digite o valor de a"))
b = float(input("digite o valor de b")) 
c = float(input("digite o valor de c"))


print(f"a equação de segundo grau é: \n\t{a}x² + {c} = 0")


#proces. de dados
delta = (b**2) - (4 * a * c)


#ve se o delta é maior que zero
if delta == 0:
    raiz =(-b + (delta)**0.5) / (2 * a)
    print("raizes iguais portanto x =" , raiz)
elif delta > 0:
    raiz1 = (-b + (delta)**0.5) / (2 * a)
    raiz2 = (-b - (delta)**0.5) / (2 * a)
    print("raiz 1 = ", raiz1)
    print("raiz 2 = ", raiz2)
else:
    print("o valor de delta é menor que 0, raizes impossiveis")