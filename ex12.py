#12 - Ler dois valores
# (considere que não serão lidos valores iguais) e escrever o maior deles.

num2=0
num1=0
repetido=True
while repetido:
    num1=int(input("digite um numero a ser comparado: "))
    num2=int(input("digite um numero a ser comparado e que não seja repetido: "))
    if num1!=num2:
        repetido=False
    else:
        print("numero igual, repita de novo\n")

if num1>num2:
    print("o numero maior é o: ",num1,", o menor é o: ",num2)
elif num2>num1:
    print("o numero maior é o: ",num2,", o menor é o: ",num1)