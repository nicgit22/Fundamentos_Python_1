try:
    dias = int(input("digite o numero de dias: "))

    anos = dias//365
    mes = (dias % 365)// 30
    dia = (dias % 30) % 30

    print(f"{anos} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{dia} dia(s)")
except:
    print("digite um valor valido")
