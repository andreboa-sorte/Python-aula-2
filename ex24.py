'''24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas,
 isto é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
'''

listaUm=[]
listaDois=[]
tudo=[]
inter=[]
index=0
menu=True
while menu:
    op=int(input("1- adicionar num na lista 1°\n"
                 "2- adicionar num na lista 2°\n"
                 "3- printar lista 1°\n"
                 "4- printar lista 2°\n"
                 "5- união das duas\n"
                 "6- lista intercalada\n"
                 "7- sair\n"
                 "opção: "))
    if op ==1:
        numero=int(input("digite um numero: "))
        listaUm.append(numero)

    elif op==2:
        numeros=int(input("digite um numero: "))
        listaDois.append(numeros)
        index=index+1

    elif op==3:
        print("lista um: ")
        for i in range(len(listaUm)):
            print(listaUm[i])

    elif op==4:
        print("lista dois: ")
        for i in range(len(listaDois)):
            print(listaDois[i])

    elif op==5:
        for i in range(len(listaUm)):
            tudo.append(listaUm[i])
        for i in range(len(listaDois)):
            tudo.append(listaDois[i])
        print("lista união: ")
        for i in range(len(tudo)):
            print(tudo[i])

    elif op==6:
        for i,j in zip(listaUm,listaDois):
            inter.append(i)
            inter.append(j)


        print("lista intercalada: ")
        for i in range(len(inter)):
            print(inter[i])

    elif op==7:
        menu=False

