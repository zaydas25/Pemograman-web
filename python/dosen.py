from person import *

class dosen(person):
    gelar = "S.Pd"
    jabatan = "Dosen"
    gaji = 0

    def __init__(self, name, gender, age, gelar, jabatan = "Dosen"):
        super().__init__(name, gender, age)
        self.gelar = gelar
        self.jabatan = jabatan

    def setgaji(self, nominal):
        self.__gaji = nominal

    def cetak(self):
        super().cetak()
        print("Gaji \t\t: Rp.", self.__gaji,
            "\nJabatan \t:", self.jabatan,
            "\nGelar \t\t:", self.gelar)

dosen1 = dosen("Sulaiman", "Laki-laki", 30,"S.Pd")
dosen1.setgaji(5000000)
dosen1.cetak()