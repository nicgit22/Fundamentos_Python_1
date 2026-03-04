import produto as p

#criar obj do tipo produto
play = p.Produto()

#entrada de dados

print("entre os dados do produto: ")
play.nome = input("nome: ")
play.preco = float(input("Preço: R$"))
play.quantidade = int.input("Quantidade: ")


#saida de dados#1
print("Dados do produto: ")
print(play.saida_de_dados())


#saida de dados#2
quantidade = int(input("digite a quatidade a ser adicionada ao estoque: "))
print("dados atualizados")
play.remover_produtos(quantidade)
print(play.saida_de_dados())

#pip install streamlit