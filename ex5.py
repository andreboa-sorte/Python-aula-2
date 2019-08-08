class Numero():

    def numero_(self):

        num=int(input('digite um numero para ser lido: '))
        imp_par= num%2

        if ((num>0)and (imp_par!=0)):
            print('o numero é positivo e é impar')

        elif ((num<0) and (imp_par!=0)):
            print('o numero é negativo e é impar')

        elif ((num>0)and(imp_par==0)):
            print('o numero é positivo e par')

        elif  ((num<0)and(imp_par==0)):
            print('o numero é negativo e par')

chama=Numero()

menu=True

while menu:
    op=int(input('\n1- digitar numero \n'
                 '2- sair \n'
                 'opção: '))
    if op==1:
        chama.numero_()

    elif op==2:
        menu=False
