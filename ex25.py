'''25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos
 da primeira metade
'''

lista=[]
num=0
listacomum=[]
index=0
i=0

menu=True
while menu:
    op=int(input("1- adicionar num na lista\n"
                 "2- printar metade na frente\n"
                 "3- printar comum\n"
                 "4- sair\n"
                 "opção: "))
    if op==1:
        num=int(input("digite um numero: "))
        lista.append(num)
        listacomum.append(num)

        index=index+1

    elif op==2:
        aux=index/2
        aux=index
        aux=round(aux)

        print("lista metade na frente:")

        for aux in range(aux>=index):
            print(listacomum[aux])

        for i in range(i>aux):
            print(listacomum[i])

    elif op==3:
        print(listacomum)

    elif op==4:
        menu=False
