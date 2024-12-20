def infosuhu():
    lokasi = input("Lokasi: ")
    suhu = float(input("Suhu: "))
    def status():
        if suhu < 0: kondisi = "beku"
        elif suhu >= 0 and suhu <= 15: kondisi = "dingin"
        elif suhu > 15 and suhu <= 25: kondisi = "sejuk"
        elif suhu > 25 and suhu <= 30: kondisi = "biasa"
        else: kondisi = "panas"
        return kondisi
    print('---------- Informasi Suhu ----------',
          '\nLokasi\t:', lokasi,
          '\nSuhu\t:', suhu,
          '\nKondisi\t:', status())
    
#panggil suhu
infosuhu()