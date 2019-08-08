class Caixa():

    def troco(self):

        clie=float(input('digite o dinhero que o cliente entregou: '))

        produto=float(input('digite o preço do produto: '))

        troco= clie-produto

        print('o troco a ser dado é: {0:.2f}'.format(troco))

    def troco_desconto(self):
        clie=float(input('digite o dinhero que o cliente entregou: '))

        produto=float(input('digite o preço do produto: '))

        disc=int(input('digite quantos % de desconto se deja dar: '))

        troco= clie - (produto-(produto/disc))

        print('o troco a ser dado é: {0:.2f}'.format(troco))


chama=Caixa()

menu=True

while menu:
    op=int(input('\n1- troco sem desconto \n'
                 '2- troco com desconto \n'
                  '3- sair \n'
                 'opção: '))

    if op==1:
         chama.troco()

    elif op==2:
        chama.troco_desconto()

    elif op==3:
        menu=False
         
    
