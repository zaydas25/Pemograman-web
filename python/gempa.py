class gempa:
    lokasi = ""
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if(self.skala < 2):
            ket = "Tidak ada dampak"
        elif(self.skala >= 2 and self.skala < 4):
            ket = "kerusakan ringan"
        elif(self.skala >= 4 and self.skala < 5):
            ket = "Kerusahan serius"
        elif(self.skala == 10):
            ket = "AZAB YANG PEDIH"
        else:
            ket = "Kerusahan besar dan berpotensi Tsunami"
        
        print("telah terjadi gempa di",self.lokasi,
            "dengan skala",self.skala,
            "Ritcher "
            "Dengan",ket)

banten = gempa('Banten', 1.2)
jepang = gempa('Jepang', 4.3)
israel = gempa('Israel', 10)

banten.dampak()
jepang.dampak()
israel.dampak()