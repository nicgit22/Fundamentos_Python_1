SENHA = 2002
contagem = 0
senha = int(input("digite a senha"))

while (senha != SENHA):
    senha = int(input("senha invalida"))
    contagem += 1
    if (contagem > 3):
        print("numero de tentativas execedidos")
        break#interrompe o codigo
print("acesso liberado")


