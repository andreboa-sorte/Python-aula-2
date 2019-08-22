#  18 - Crie uma classe animal com o método comer,
#  este método deve  escrever na tela "o animal esta comendo".
#  Depois disso crie as classes cachorro, cavalo e gato e
# implemente o método comer de acordo com o que cada animal come.
# Crie uma classe AnimalTeste e coloque os três animais dentro de
# uma lista de animais e chame o método comer polimorficamente (com um for)

class Zoo:
    cavalo=''
    comida=''
    gato=''
    cachorro=''
    def chama_para_comer(self):
        comida='o animal esta comendo...'
    def animais(self):
        cavalo='cavalo '
        gato='gato '
        cachorro='cachorro '
    def animal_teste(self):
        print(cavalo)

chama=Zoo()
chama.chama_para_comer()
chama.animais()
chama.animal_teste()
