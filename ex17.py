#17 - Cria uma lista para armazenar 5 nomes fixos. Após inserir os
# 5 nome da lista mostre-os no console (utilize um for).
nomes=[]
nome=""
for i in range(5):
    nome=input("digite um nome: ")
    nomes.append(nome)
print("lista dos nomes:")
for i in range(len(nomes)):
    print(nomes[i])