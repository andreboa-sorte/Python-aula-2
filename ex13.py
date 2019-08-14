#  13 - Escreva um algoritmo que leia as idades de 2 homens e
#  de 2 mulheres (considere que as idades dos homens serão sempre
#  diferentes entre si, bem como as das mulheres).
#  Calcule e escreva a soma das idades do homem mais velho com
#  a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.
class Idade():
   def dois_m_w(self):
        homen2=0
        homen1=0
        Mnovo=0
        Wnova=0
        mulher1=0
        mulher2=0
        Widade=0
        Midade=0
        situacao=True
        while situacao:
            homen1 = int(input("digite a idade do primeiro homeme: "))
            homen2 = int(input("digite a idade do segndo homeme, DIFERENTE DO PRIMEIRO: "))
            if homen1!= homen2:
                situacao=False
        if homen2>homen1:
             Midade=homen2
             Mnovo=homen1
        else:
            Midade=homen1
            Mnovo = homen2
        print("\n")
        situacao2 = True

        while situacao2:
            mulher1=int(input("digite a idade da primeira mulher: "))
            mulher2 = int(input("digite a idade da segunda mulher, DIFERENTE DA PRIMEIRA: "))
            if mulher1!=mulher2:
                situacao2=False
        if mulher1>mulher2:
            Widade=mulher1
            Wnova=mulher2
        elif mulher2>mulher1:
            Widade=mulher2
            Wnova = mulher1

        soma1=Midade+Wnova
        soma2=Widade+Mnovo
        print("a soma das idades do homem mais velho com"
              "a mulher mais nova é: ",soma1)
        print("e o produto das idades do homem mais novo com "
              "a mulher mais velha é: ",soma2)
chama=Idade()
menu=True
while menu:
    op=int(input("1- calcular as idades\n"
                 "2- sair\n"
                 "opção: "))
    if op==1:
        chama.dois_m_w()
    elif op==2:
        menu=False





