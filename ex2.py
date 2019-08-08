class Extenso():
    def chama_extenso(self):
        num=int(input('digite um numero entre 1 a 5, para se tornar extenso: '))
        if num==1:
            print("Um")
        elif num==2:
            print("Dois")
        elif num==3:
            print("Tres")
        elif num==4:
            print("Quatro")
        elif num==5:
            print("Cinco")
        elif num>5:
            print('numero invalido')
        elif num<1:
            print('numero invalido')

chama=Extenso()

menu=True

while menu:
    op=int(input('\n1- digitar numero \n'
                 '2- sair \n'
                 'opção: '))
    if op==1:
        chama.chama_extenso()

    elif op==2:
        menu=False
