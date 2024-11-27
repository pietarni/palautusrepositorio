KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if isinstance(kapasiteetti, int) and kapasiteetti >= 0:
            self.kapasiteetti = kapasiteetti
        else:
            self.kapasiteetti = KAPASITEETTI

        if isinstance(kasvatuskoko, int) and kasvatuskoko >= 0:
            self.kasvatuskoko = kasvatuskoko
        else:
            self.kasvatuskoko = OLETUSKASVATUS

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == numero:
                return True
        return False

    def lisaa(self, numero):
        if not self.kuuluu(numero):
            if self.alkioiden_lkm >= len(self.ljono):
                self._laajenna()
            self.ljono[self.alkioiden_lkm] = numero
            self.alkioiden_lkm += 1
            return True
        return False

    def _laajenna(self):
        uusi_lista = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, numero):
        poistettava_indeksi = -1

        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == numero:
                poistettava_indeksi = i
                self.ljono[poistettava_indeksi] = 0
                break

        if poistettava_indeksi != -1:
            self._siirra_vasemmalle(poistettava_indeksi)
            self.alkioiden_lkm -= 1
            return True
        return False

    def _siirra_vasemmalle(self, indeksi):
        for j in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[j] = self.ljono[j + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def kopioi_lista(self, lähde, kohde):
        for i in range(len(lähde)):
            kohde[i] = lähde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        tulos_joukko = IntJoukko()
        for numero in joukko_a.to_int_list():
            tulos_joukko.lisaa(numero)
        for numero in joukko_b.to_int_list():
            tulos_joukko.lisaa(numero)
        return tulos_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        tulos_joukko = IntJoukko()
        for numero in joukko_a.to_int_list():
            if joukko_b.kuuluu(numero):
                tulos_joukko.lisaa(numero)
        return tulos_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        tulos_joukko = IntJoukko()
        for numero in joukko_a.to_int_list():
            tulos_joukko.lisaa(numero)
        for numero in joukko_b.to_int_list():
            tulos_joukko.poista(numero)
        return tulos_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm)) + "}"
