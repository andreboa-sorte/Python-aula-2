'''22 - Crie a classe Imóvel, que possui um endereço e um preço.

a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.

b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto.
'''

class Imovel():
    def info_imovel(self):
       pass


class NovoImovel(Imovel):
    def info_imovel(self):
        endereco = " SC-401, 9301 - Santo Antonio de Lisboa, Florianópolis - SC, 88050-001"
        preco = 2000000.0


        novo_preco=float(input("digite o preço adicional do novo imovel acima do preço de {0:.2f}: ".format(preco)))

        novo_preco= preco + novo_preco

        print(" novo imovel\n"
              "preço: {0:.2f} \n"
              "endereço: {1}".format(novo_preco,endereco))

class AntigoImovel(Imovel):
    def info_imovel(self):
        endereco = " Ed.Zigurate Centro, Rua Saldanha Marinho, 374 - Centro, Florianópolis - SC, 88020-050"
        preco = 2000000.0


        novo_preco = float(input("digite o desconto do imovel antigo acima do preço de {0:.2f}: ".format(preco)))

        novo_preco = preco - novo_preco

        print(" Antigo imovel\n"
              "preço: {0:.2f} \n"
              "endereço: {1}".format(novo_preco, endereco))


menu=True

while menu:
    op=int(input("1- novo imovel\n"
                 "2- antigo movel\n"
                 "3- sair\n"
                 "opção: "))

    if op==1:
        chama=NovoImovel()

        chama.info_imovel()

    elif op==2:
        chama=AntigoImovel()

        chama.info_imovel()

    elif op==3:
        menu=False
