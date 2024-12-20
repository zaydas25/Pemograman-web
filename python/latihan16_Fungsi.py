print("----- Silakan Masukkan Data Anda -----")
def hitunggaji():
    nama = input("Masukkan Nama Anda\t: ")
    jabatan = input("Masukkan Jabatan Anda\t: ")
    agama = input("Masukkan Agama Anda\t: ")
    status = input("anda sudah menikah\t: ")

#    def gapok(jabatan):
#        return{
#            "Manager" : 15000000,
#            "Asisten Manager" : 10000000,
#            "Supervisor" : 7000000,
#            "Staff" : 4000000
#        }[jabatan]

    def gapok():
        match jabatan:
            case "Manager": return 15000000
            case "Asisten Manager": return 10000000
            case "Supervisor": return 7000000
            case "Staff": return 4000000
            case _: return 0
    tunjab = 0.3 * gapok()
    BPJS = 0.1 * gapok()

    def tunkel(s):
        match s:
            case "iya"|"ya"|"sudah": return 0.1 * gapok()
            case "tidak": return 0
            case _: return 0
    gator = gapok() + tunjab + BPJS + tunkel(status)

    def zakat():
        return (0, 0.025 * gator)[agama == "Islam" and gator >= 7000000]

    def formatgaji(gaji):
        return "{:,}".format(gaji)

    print("\n----- Hasil Perhitungan Gaji Karyawan -----")
    print("Gaji Pokok\t\t:", formatgaji(gapok()),
        "\nTunjangan Jabatan\t:", formatgaji(tunjab), 
        "\nBPJS\t\t\t:", formatgaji(BPJS), 
        "\nTunjangan Keluarga\t:", formatgaji(tunkel(status)),
        "\nTotal Gaji Kotor\t:", formatgaji(gator),
        "\nZakat\t\t\t:", formatgaji(zakat()),
        "\nGaji Bersih\t\t:", formatgaji(gator - zakat()))

hitunggaji()