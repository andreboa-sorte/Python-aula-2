class Extenso():
    def meumetodo(self):
        num = int(input('digite um numero entre 1 a 5, para se tornar extenso: '))
        return self.chama_extenso(num)

    def chama_extenso(self,num):

        if num == 1:
            return "Um"
        elif num == 2:
            return "Dois"
        elif num == 3:
            return "Tres"
        elif num == 4:
            return "Quatro"
        elif num == 5:
            return "Cinco"
        elif num > 5:
            return 'numero invalido'
        elif num < 1:
            return 'numero invalido'

  #  meumetodo()
'''
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
'''