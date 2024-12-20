class Bank:
    norek = ''
    nama = ''
    saldo = 0
    jmlNsbh = 0
    BANK = 'Bank Syariah Nurul Fikri'
    def __init__(self, no, nsbh, saldo):
        self.norek = no
        self.nama = nsbh
        self.saldo = saldo
        Bank.jmlNsbh += 1

    def tabung(self, uang):
        self.saldo += uang
    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self):
        print(Bank.BANK,
            "\n========================================",
            "\nNo. Rekening\t: ", self.norek,
            "\nNama Nasabah\t: ", self.nama,
            "\nSaldo\t\t:  Rp.",format(self.saldo, ','),
            "\n----------------------------------------"
            )
        
    def nabung(self, nominal):
        self.saldo += nominal
        print("menabung berhasil!, Saldo Anda sekarang Rp.", format(self.saldo, ','))
    def tarik(self, nominal):
        self.saldo -= nominal
        print("menarik berhasil!, Saldo Anda sekarang Rp.", format(self.saldo, ','))

Farrel = Bank('121204', 'F.A Farrel',100000000)
Bian = Bank('121205', 'Sabian',2000000)
Gilang = Bank('121206', 'M.Gilang',1000000)
Zaid = Bank('121207', 'Zaid A.S',1000000000)

Zaid.nabung(1000000)
Zaid.cetak()