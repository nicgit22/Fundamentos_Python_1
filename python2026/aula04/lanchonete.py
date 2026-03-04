codigo = int(input("digite o codigo do produto"))
quantidade = int(input("digite a quantidade comprada"))

#processamento com match case

match codigo:
    case 1:
        #5rs
        total = quantidade * 5.00
    case 2:
        total = quantidade * 3.50
    case 3:
        total  = quantidade * 4.80
    case 4:
        total = quantidade * 8.90
    case 5:
        total = quantidade * 7.32

#saida
print(f"valor a pagar = {total:.2f}")

