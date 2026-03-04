#declarar vars
base:float
altura:float
area:float
perimetro:float
diagonal:float
#entrada de dados
base = float(input("digite a base do retangulo: "))
altura = float(input("digite a altura do retangulo: "))

#processamento de dados
area = base * altura
perimetro = 2*base + 2*altura
diagonal = (base**2 + altura**2)**0.5

#saida de dados
print(f"area = {area:.2f}") #2f limita as casas após a virgula
print(f"perimetro = {perimetro}")
print(f"diagonal = {diagonal:.2f}")
