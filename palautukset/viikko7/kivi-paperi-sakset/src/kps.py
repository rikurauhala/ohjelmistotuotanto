from tuomari import Tuomari


class KiviPaperiSakset:
    def __init__(self):
        self._tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto, tokan_siirto = self._hae_siirrot()
        while self._ok_siirrot(ekan_siirto, tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._tulosta_tilanne()
            ekan_siirto, tokan_siirto = self._hae_siirrot()
        self._paata_peli()

    def _hae_siirrot(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto()
        return ekan_siirto, tokan_siirto

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        pass

    def _ok_siirrot(self, ekan_siirto, tokan_siirto):
        return self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    def _tulosta_tilanne(self):
        print(self._tuomari)

    def _paata_peli(self):
        print("Kiitos!")
        self._tulosta_tilanne()
