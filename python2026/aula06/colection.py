lista = ["senai", True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[1])
print(len(lista))
del lista[2]
print(lista)
lista.insert(2, "SENAII")
lista.append("eduane")
print(lista)
#pode--repetir--dados


#------------------tupla---------------------
tupla = ("senal", False, 24, 1.73)
print(tupla)
print(type(tupla))
print(tupla[3])
#tupla é imutavel


#---------dicionario-----------
dicionario = {"nome":  "senai", "logica": True, "numero":2, "n":2.75}
print(dicionario)
print(type(dicionario))
dicionario.update()


#------conjunto-----
conjunto = {"senai", True, 10, 2.1}
print(conjunto)
print(type(conjunto))
#não indexada e ordenada