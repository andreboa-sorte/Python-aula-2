'''23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos
'''

lista=[]
numero=0
todos=0
index=0
media=0

menu=True

while menu:
    op=int(input("1- adicionar um numero na lista\n"
                 "2- sair do loop\n"
                 "opção: "))
    if op==1:
        numero=int(input("digite um numero inteiro: "))
        lista.append(numero)

    elif op==2:
        menu=False

for i in range(len(lista)):
    todos=todos+lista[i]
    index=index+1

media=todos/index

print("Resultados da lista:")
print("o maior numero: ",max(lista))
print("o primiero numero da lista é: ",lista[0])
print("a toma de todos é: ",todos)
print("a media de todos é: ",media)
