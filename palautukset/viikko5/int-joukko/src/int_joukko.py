class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self._validoi_parametrit(kapasiteetti, kasvatuskoko)
        self._kapasiteetti = kapasiteetti
        self._kasvatuskoko = kasvatuskoko
        self._luvut = [0 for _ in range(self._kapasiteetti)]
        self._mahtavuus = 0

    def _validoi_parametrit(self, kapasiteetti, kasvatuskoko):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava positiivinen kokonaisluku!")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen kokonaisluku!")

    def kuuluu(self, n):
        return n in self._luvut

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if self._mahtavuus == 0:
            self._luvut[0] = n
            self._mahtavuus += 1
            return True
        self._luvut[self._mahtavuus] = n
        self._mahtavuus += 1
        if self._mahtavuus % len(self._luvut) == 0:
            taulukko_old = self._luvut
            self.kopioi_taulukko(self._luvut, taulukko_old)
            self._luvut = [0 for _ in range(self._mahtavuus + self._kasvatuskoko)]
            self.kopioi_taulukko(taulukko_old, self._luvut)
        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        indeksi = self._luvut.index(n)
        self._luvut[indeksi] = 0
        for j in range(indeksi, self._mahtavuus-1):
            apu = self._luvut[j]
            self._luvut[j] = self._luvut[j+1]
            self._luvut[j+1] = apu
        self._mahtavuus -= 1
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self._mahtavuus

    def to_int_list(self):
        return [luku for luku in self._luvut if luku > 0]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus.poista(b_taulu[i])

        return erotus

    def __str__(self):
        return f"{{{', '.join([str(luku) for luku in self._luvut if luku > 0])}}}"
