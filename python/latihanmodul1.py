def luaslingkaran():
    jari = int(input("Masukkan jari-jari lingkaran: "))
    hitung = 3.14 * (jari ** 2)
    print(f"Luas lingkaran dengan jari-jari {jari} cm adalah, {hitung}")

def luaspersegi():
    sisi = int(input("Masukkan sisi persegi: "))
    hitung = sisi * sisi
    print(f"Luas persegi dengan sisi {sisi} cm adalah, {hitung}")

def luassegitiga():
    alas = int(input("Masukkan alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))
    hitung = (alas * tinggi) / 2
    print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah, {hitung}")

import latihanmodul1
def main():
    while True:
        pilihan = str(input("Masukkan pilihan (1 lingkaran / 2 persegi / 3 segitiga) : "))
        if pilihan == "1":
            latihanmodul1.luaslingkaran()
        elif pilihan == "2":
            latihanmodul1.luaspersegi()
        elif pilihan == "3":
            latihanmodul1.luassegitiga()
        else:
            print("Pilihan tidak tersedia")
            break
main()
