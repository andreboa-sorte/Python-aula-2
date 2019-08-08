class MadiaAluno():

    def cacula_media(self):

            nota1=float(input("digite a primeira nota do aluno: "))

            nota2=float(input("digite a segunda nota do aluno: "))

            nota3=float(input("digite a terceira nota do aluno: "))

            media=((nota1+nota2+nota3)/3)

            print("a media do aluno é: {0:.2f}".format(media))

chama=MadiaAluno()

situacao=True

while situacao:
    op=int(input("1- calcular a media do aluno\n"
                 "2- sair\n"
                 "opção: "))
    if op==1:
        chama.cacula_media()

    if op==2:
        situacao=False




