from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


class Peli:
    def __init__(self, pelimuoto):
        self._pelimuoto = pelimuoto
        self._peli = None

    def pelaa(self):
        match self._pelimuoto:
            case 'a':
                self._peli = KPSPelaajaVsPelaaja()
            case 'b':
                self._peli = KPSTekoaly()
            case 'c':
                self._peli = KPSParempiTekoaly()
            case _:
               return
        self._tulosta_ohjeet()
        self._peli.pelaa()

    def _tulosta_ohjeet(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

    @staticmethod
    def pelaaja_vs_pelaaja():
        return Peli('a')

    @staticmethod
    def pelaaja_vs_tekoaly():
        return Peli('b')
    
    @staticmethod
    def pelaaja_vs_parempi_tekoaly():
        return Peli('c')
