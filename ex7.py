#7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o
#menor, número, o maior número,a soma dos números informados e
# a média aritmética dos números informados.
numeros=[]
class DezNumeros():

    def input_numeros(self):
        for i in range(10):
            numero=int(input("digite um numero: "))
            numeros.append(numero)

    def print(self):
        menor = 999
        maior = 0
        media_aritimetica=0
        index=0
        soma_todos=0
        for i in range(len(numeros)):
            if numeros[i]>maior:
                maior=numeros[i]
            elif numeros[i]<menor:
                menor=numeros[i]
            index=index +1
            soma_todos=soma_todos+numeros[i]
            media_aritimetica=soma_todos/index
        print("o maior numero é o: ",maior)
        print("o menor numero é o: ",menor)
        print("a media aritimetica é: ",media_aritimetica)



chama=DezNumeros()

menu=True

while menu:
    op = int(input('1- digitar 10 numeros \n'
                   '2- printar resultado \n'
                   '3- sair\n'
                   'opção: '))
    if op==1:
        chama.input_numeros()
    elif op==2:
        chama.print()
    elif op==3:
        menu=False