#15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

numeros=[]
index=0
while index<10:
    numero=int(input("digite um numero a ser comparado que não seja repetido: "))
    if numero in numeros:
        print("por favor, digite um numero não repetido")
    else:
        index=index+1
        numeros.append(numero)
maior=max(numeros)
print("o maior numero é:{} ".format(maior))
