import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassassa_rahaa_1000_euroa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lounaita_myyty_0(self):
        self.assertTrue(self.kassapaate.edulliset == 0 and self.kassapaate.maukkaat == 0)    

    def test_syo_edullisesti_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1002.40)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(340) == 100)

    def test_syo_edullisesti_kateisella_lounaat_kasvavat(self):
        kassapaate = self.kassapaate
        lounas1 = kassapaate.edulliset
        kassapaate.syo_edullisesti_kateisella()
        self.assertEqual(self.kassapaate.edulliset == lounas + 1)
    

