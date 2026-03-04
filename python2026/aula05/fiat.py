
import time as t
veiculos = 0
turistas = 0

print("Aplicativo de controle de fluxo carros")
print("Parque Nacional os Lençóis Maranhenses\n")

print("Bem-Vindo ao aplicativo de controle de fluxo carros!")

while True:
    fluxo = input("Digite o fluxo de carro (entrando/voltando) ou sair para encerrar: ")
    if fluxo == "sair":
        break
    quantidade = int(input("Digite o número de turistas: "))
    if fluxo == "entrando":
        veiculos += 1
        turistas += quantidade
        print("entrada registrada em") 
        print(t.ctime(t.time()));
    elif fluxo == "voltando":
        veiculos -= 1
        turistas -= quantidade
        print("volta registrada em") 
        print(t.ctime(t.time()));

    print("Turistas que ainda não voltaram", turistas)
    print("Veiculos que ainda não voltaram", veiculos)


