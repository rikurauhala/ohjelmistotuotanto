import unittest

from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.piima = Tuote("Piimä", 2)

    # Vaihe 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # Vaihe 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # Vaihe 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), self.maito.hinta())

    # Vaihe 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # Vaihe 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikea(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)
        self.assertEqual(self.kori.hinta(), self.maito.hinta() + self.piima.hinta())

    # Vaihe 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # Vaihe 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikea(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 2 * self.maito.hinta())

    # Vaihe 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # Vaihe 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_oikeat_tiedot(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    # Vaihe 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    # Vaihe 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # Vaihe 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_samaa_tuotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    # Vaihe 13
    def test_toisen_tuotteen_poistaminen_jattaa_koriin_ostoksen_jossa_yksi_tuote(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)
        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    # Vaihe 14
    def test_tuotteen_poistaminen_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 0)

    # Vaihe 15
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.piima)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
        self.assertEqual(ostokset[0].lukumaara(), 3)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
