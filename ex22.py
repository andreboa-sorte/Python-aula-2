'''22 - Crie a classe Imóvel, que possui um endereço e um preço.

a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.

b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto.
'''

class Imovel():
    def info_imovel(self):
        endereco=" SC-401, 9301 - Santo Antonio de Lisboa, Florianópolis - SC, 88050-001"
        preco=2000000.0


class NovoImovel(Imovel):
    def info_novo_imovel(self,preco):
        novo_preco=float(input("digite o preço adicional do novo imovel acima do preço de {0:.2f}: ".format(preco)))

        novo_preco=novo_preco + preco
