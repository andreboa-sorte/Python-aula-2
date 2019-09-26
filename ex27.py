'''27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v
w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um
método para "traduzir", que recebe uma lista com uma mensagem (secreta) e "traduz"
 a sequência armazenada em uma lista.
'''

dicionario={0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
            11: 'k', 12: 'l',13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
            21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
msg=[]

situacao=True

while situacao:
    op=int(input("1- digitar o codigo\n"
                 "2- sair\n"
                 "opção: "))

    if op==1:
        num=int(input("digite a mensague a ser taduzida: "))
        msg.append(num)

    elif op==2:
        situacao=False

for i in range(len(msg)):
    print(dicionario[msg[i]], end='')