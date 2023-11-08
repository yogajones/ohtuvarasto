import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktorille_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktorille_negatiivinen_alkusaldo(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        saldo_ennen_lisaysta = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo_ennen_lisaysta)

    def test_ylitaytto_tayttaa_varaston(self):
        # ylitäyttö täyttää varaston ja loppu menee hukkaan
        self.varasto.lisaa_varastoon(1 + self.varasto.paljonko_mahtuu())
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_ei_muuta_mitaan(self):
        self.varasto.lisaa_varastoon(3)
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_liikaotto_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liikaotto_palauttaa_sen_mita_voi(self):
        # liian suuri otto palauttaa varaston saldon täsmälleen
        self.varasto.lisaa_varastoon(3)
        saldo_ennen_ottoa = self.varasto.saldo
        self.assertAlmostEqual(
            self.varasto.ota_varastosta(8), saldo_ennen_ottoa)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_(self):
        self.assertAlmostEqual(self.varasto.__str__(
        ), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
