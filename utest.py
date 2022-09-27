import unittest
import zadanie

class TestMainMethod(unittest.TestCase):
    
    def test_dodaj(self):
        s=zadanie.dodaj(2,2,2)
        self.assertEqual(s,6)


    def test_wpis_imie(self):
        im=zadanie.wpisz_imie('Artur')
        self.assertEqual(im,'Dzien dobry ARTUR')
        
    def test_pole_kola(self):
       pk=zadanie.pole_kola(2)
       self.assertEqual(pk,12.56)
        
