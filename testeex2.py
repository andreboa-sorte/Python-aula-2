from ex2 import Extenso
import unittest

class testeextenso(unittest.TestCase):
    def test_numeroextenso(self):
        MeuNumero=Extenso()
        resultado=MeuNumero.chama_extenso(1)
        self.assertEquals(resultado,"Um")
