import math 
def tambah(bil1,bil2):
    hasil = bil1 + bil2
    print("Hasil penjumlahan dari %i + %i = %i" %(bil1,bil2,hasil))

def kurang(bil1,bil2):
    hasil = bil1 - bil2
    print("Hasil penngurangan dari %i - %i = %i" %(bil1,bil2,hasil))

def kali(bil1,bil2):
    hasil = bil1 * bil2
    print("Hasil perkalian dari %i x %i = %i" %(bil1,bil2,hasil))

def bagi(bil1,bil2):
    hasil = bil1 / bil2
    print("Hasil pembagian dari %i : %i = %i" %(bil1,bil2,hasil))

def pangkat(bil1,bil2):
    hasil = math.pow(bil1,bil2)
    print("Hasil pemangkatan dari %i ^ %i = %i" %(bil1,bil2,hasil))
