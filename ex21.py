'''21 - mostrando na tela o valor. Depois disso, crie uma classe de testes instanciando os objetos programador e analista e ch
Crie uma classe chamada Ingresso que possui um valor em reais e um método
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

    def ingresso_vip(self):
        valor_temp=float(input("digite o valor adiciona do camarote vip com relação "
                               "ao ingresso normal {0:.2f}".format(salario)))

        ingresso_vip = valor_temp + valor_ingresso

        print("o preço do ingresso VIP é {0:.2f}".format(ingresso_vip))

    def ingresso_normal(self):


