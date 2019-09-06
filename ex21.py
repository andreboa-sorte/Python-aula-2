'''21 -Crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor().

a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).

b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".

c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos

para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIPame.
'''

class Ingresso():
    valor_ingresso=200.00


class IngressoVip(Ingresso):
    def ing_vip(self):
        valor_temp=float(input("digite o valor adiciona do camarote vip com relação "
                               "ao ingresso normal {0:.2f}".format(salario)))

        ingresso_vip = valor_temp + valor_ingresso

        print("o preço do ingresso VIP é {0:.2f}".format(ingresso_vip))

class IngressoNormal(Ingresso):
    def ing_normal(self):
        print("o preço do ingresso normal é de {0:.2f}",format(valor_ingresso))


class CamaroteInferior(Ingresso):
    def camarote_inf(self):
        preco_temp=float(input('digite o preço adicional do camarote inferior com relação ao preco normal de {0:.2f}'.format(valor_ingresso)))
        local_cam_inf=input("digite o local onde se solcaliza o camarote inferior: ")

        cama_inf=preco_temp + valor_ingresso

        print("o preço do camarote inferior é de {0:.2f} e esta localizado {1}".format(cama_inf,local_cam_inf))

class CamaroteSuperior(Ingresso):
    def camarote_sup(self):
        preco_temp = float(input( 'digite o preço adicional do camarote superior com relação ao preco normal de {0:.2f}'.format(
                valor_ingresso)))
        local_cam_sup = input("digite o local onde se solcaliza o camarote superior: ")

        cama_sup = preco_temp + valor_ingresso

        print("o preço do camarote superior é de {0:.2f} e esta localizado {1}".format(cama_sup, local_cam_sup))



