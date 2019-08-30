from ex1_media5Alunos import MediaAluno
import unittest
class testeuni(unittest.TestCase):

    def teste_media(self):
        MinhaMedia=MediaAluno()
        resultado=MinhaMedia.calculo_media(5,5,5)
        self.assertEquals(resultado,5)
