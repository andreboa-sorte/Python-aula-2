#  18 - Crie uma classe animal com o método comer,
#  este método deve  escrever na tela "o animal esta comendo".
#  Depois disso crie as classes cachorro, cavalo e gato e
# implemente o método comer de acordo com o que cada animal come.
# Crie uma classe AnimalTeste e coloque os três animais dentro de
# uma lista de animais e chame o método comer polimorficamente (com um for)

class Zoo:
    def chama_para_comer(self):
        comida='o animal esta comendo...'

class Cavalo():
    def comida_cav(self):
        print("o cavalo esta comendo feno")

class Cachorro():
    def comida_toto(self):
        print("o cachorro esta comendo ração")

class Gato():
    def comida_gato(self):
        print('o gato esta comendo peixe')


chama=Zoo()
