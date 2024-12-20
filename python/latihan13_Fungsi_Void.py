#membuat function void define by user
def hitungumur(thn_now):
    nama = input("Masukkan Nama Anda : ")
    thn_lahir = int(input("Masukkan Tahun Lahir Anda : "))
    print("Mahasiswa a.n %s yg lahir tahun %i"
          " saat ini berumur %2.f" %(nama,thn_lahir,umur))
    
#panggil fungsi
hitungumur(2024)