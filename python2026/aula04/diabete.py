#entrada
glicose =  float(input("digite a medida da sua glicose"))



#proscesamento
if glicose <= 100:
    saida = "normal"
elif (glicose > 100) and (glicose <= 140):
    saida = "elevada"
else:
    saida = "diabetes"


#saida

print(f"classificação: {saida}")