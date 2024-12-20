class person:
    nama = ""
    kelamin = ""
    umur = 0

    def __init__(self, name, gender, age):
        self.nama = name
        self.kelamin = gender
        self.umur = age

    def cetak(self):
        print("Nama \t\t:", self.nama, 
            "\nKelamin \t:", self.kelamin, 
            "\nUmur \t\t:", self.umur)
        
person1 = person("Zaid", "Laki-laki", 12)
person1.cetak()