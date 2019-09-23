'''26 - Faça um programa que receba duas listas e retorne True
 se são iguais ou False caso contrário, além do número de ocorrências
  do primeiro elemento da lista.
'''

lista_um=[]
lista_dois=[]
ium=0
idois=0
i=0

menu=True
while menu:
    op=int(input("1- adicionar numero na lista 1°\n"
                 "2- adicionar numero na lista 2°\n"
                 "3- ver se é igual as duas listas\n"
                 "4- sair\n"
                 "opção: "))

    if op ==1:
        num=int(input("digite um numero da lista 1°: "))
        lista_um.append(num)

        if ium==0:
            primeiro=num

        ium+=1


    elif op==2:
        num_dois = int(input("digite um numero da lista 2°: "))
        lista_dois.append(num_dois)

        if idois==0:
            primeiro=num_dois

        idois+=1

    elif op==3:
        if ium!=idois:
            print("as listas não tem o mesmo tamanho, portanto são diferentes")
            exit()
        for i in range(len(lista_um)):
            if lista_um[i] != lista_dois[i]:
                print("numero: {0} da lista um e o numero: {1} da lista dois são diferentes!! "
                      .format(lista_um[i],lista_dois[i]))
                exit()

        print("todos os valores são iguais nas duas listas")
        print("as duas listas tem os dois tamanhos")



    elif op==4:
        menu=False