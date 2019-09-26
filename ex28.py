'''28 - Faça um programa que percorre uma lista e exiba na tela o valor mais
próximo da média dos valores da lista. Exemplo: lista = [2.5, 7.5, 10.0, 4.0]
(média = 6.0). Valor mais próximo da média = 7.5'''

lista=[2.5, 7.5, 10.0, 4.0]

aux=0
num_p=0
media=0
index=0
for i in range(len(lista)):
    media+=lista[i]
    index+=1

media=media/index

valor_p = abs(lista[0] - media)

for i in range(len(lista)):
    aux=abs(lista[i] - media)
    if aux< valor_p: #abs é valor absoluto, só pega o valor e n o sinal
        valor_p = aux
        num_p = lista[i]


print("o numero mais proximo da media é o: ",num_p)
