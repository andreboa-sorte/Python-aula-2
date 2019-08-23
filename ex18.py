#  18 - Crie uma classe animal com o método comer,
#  este método deve  escrever na tela "o animal esta comendo".
#  Depois disso crie as classes cachorro, cavalo e gato e
# implemente o método comer de acordo com o que cada animal come.
# Crie uma classe AnimalTeste e coloque os três animais dentro de
# uma lista de animais e chame o método comer polimorficamente (com um for)

class Zoo:
    def chama_para_comer(self):
        print('o animal esta comendo...')

class Cavalo(Zoo):
    def chama_para_comer(self):
        print("o cavalo esta comendo feno")


class Cachorro(Zoo):
    def chama_para_comer(self):
        print("o cachorro esta comendo ração")

class Gato(Zoo):
    def chama_para_comer(self):
     print('o gato esta comendo peixe')

class AnimalTeste():
    lista_animais=[Gato(),Cavalo(),Cachorro()]
    def animal_final(self):
        for animal in self.lista_animais:
            animal.chama_para_comer()

animais=AnimalTeste()
animais.animal_final()



