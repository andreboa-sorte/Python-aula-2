class MediaAluno():

    def calcula_media(self):

            nota1=float(input("digite a primeira nota do aluno: "))

            nota2=float(input("digite a segunda nota do aluno: "))

            nota3=float(input("digite a terceira nota do aluno: "))

            media = self.calculo_media(nota1, nota2, nota3)

            print("a media do aluno é: {0:.2f}".format(media))

    def calculo_media(self, nota1, nota2, nota3):
        media = ((nota1 + nota2 + nota3) / 3)
        return media

'''
chama=MediaAluno()

situacao=True

while situacao:
    op=int(input("1- calcular a media do aluno\n"
                 "2- sair\n"
                 "opção: "))
    if op==1:
        chama.calcula_media()

    if op==2:
        situacao=False

'''



