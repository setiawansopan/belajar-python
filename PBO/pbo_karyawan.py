class Karyawan:
    '''kelas karyawan'''
    jumlah_karyawan = 0

    #konstruktor / init
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1
    
    def tampilkan_jumlah(self):
        print("Total karyawan : ", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Gaji : ", self.gaji)

#Membuat objek dari kelas karyawan
karyawan1 = Karyawan("Arfinda", 5000000)
karyawan2 = Karyawan('Umi Khoiriyah', 6000000)

#menampilkan objek dalam kelas
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()

#tampilkan jumlah
karyawan1.tampilkan_jumlah()
