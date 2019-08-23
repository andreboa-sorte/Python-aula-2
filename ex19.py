'''
19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos: quantidadeMarchas(); tipoFreio() e marca();
 Crie também duas classes que estendem esta classe, uma se chamará BicicletaPasseio e a outra BicicletaProfissional.
  Para ﬁnalizar crie uma classe onde deverá estar o método main e crie uma instancia de cada tipo de bicicleta e
   mostre o resultado dos métodos.
'''
class Bicicleta():
    def quantidade_marchas(self):


    def tipo_freio(self):

    def marca(self):


class BicicletaPasseio(Bicicleta):

    def quantidade_marchas(self):
        print("Marchas: 21 Velocidades")

    def tipo_freio(self):
        print("Tipo de Freio: Freio a Disco Mecânico 160mm")

    def marca(self):
        print("Marca: DROPP ")


class BicicletaProfissional(Bicicleta):

    def quantidade_marchas(self):
        print("Marchas: 27 Marchas")

    def tipo_freio(self):
        print("Tipo de Freio: Freio Hidráulico Shimano")

    def marca(self):
        print("Marca: Caloi ")



