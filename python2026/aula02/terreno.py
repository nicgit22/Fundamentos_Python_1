#declarar var
largura:float
comprimento:float
preco:float
area:float
#entrada de dados
largura = float(input("digite a largura do terreno: ")) #conversão de str para float
comprimento = float(input("digite o comprimento do terreno: "))
preco = float(input("digite o preço do metro quadrado do terreno: R$"))

#processamento de dados
area = largura * comprimento
valor = preco * area

#saida de dados
print(f"a area do terreno é de {area} m²")
print(f"o valor do terreno pe de R$ {valor}")