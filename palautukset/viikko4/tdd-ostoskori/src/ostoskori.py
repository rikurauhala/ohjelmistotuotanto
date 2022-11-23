from ostos import Ostos
from tuote import Tuote


class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        if not self._ostokset:
            return 0
        tavaroita = 0
        for tuote in self._ostokset:
            ostos = self._ostokset[tuote]
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        hinta = 0
        for tuote in self._ostokset:
            ostos = self._ostokset[tuote]
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        tuote = lisattava.nimi()
        if tuote not in self._ostokset:
            uusi_ostos = Ostos(lisattava)
            self._ostokset[tuote] = uusi_ostos
        else:
            self._ostokset[tuote].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        tuote = poistettava.nimi()
        self._ostokset[tuote].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self):
        ostokset = []
        for ostos in self._ostokset.values():
            ostokset.append(ostos)
        return ostokset
