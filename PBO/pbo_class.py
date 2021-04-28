#kelas / template / blue print
class siswa:
    #atribut kelas / variabel
    jumlah_siswa = 0

    #methode
    def __init__(self, inputNama, inputKelas, inputNilai): #init / konstruktor
        self.nama = inputNama
        self.kelas = inputKelas
        self.nilai = inputNilai
        siswa.jumlah_siswa += 1

    def tampilSiswa(self):
        print("Nama  : ", self.nama)
        print("Kelas : ", self.kelas)
        print("------------")
    
    def tampilNilai(self):
        print("Nama  : ", self.nama)
        print("Nilai : ", self.nilai)
        print("------------")


#instansiasi objek
udin = siswa("Suparudin", "XI MIPA 1", 90)
susi = siswa("Susi Susanti", "XI MIPA 2", 92)

udin.tampilSiswa()
udin.tampilNilai()

susi.tampilSiswa()
susi.tampilNilai()
