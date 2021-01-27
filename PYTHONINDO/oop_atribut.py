class Karyawan:
    """ dasar kelas untuk semua karyawan """
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan : ", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Gaji : ", self.gaji)

karyawan1 = Karyawan("Sopan Setiawan", 3000000)
karyawan2 = Karyawan("Arfinda Ilmania", 3500000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan : ", Karyawan.jumlah_karyawan)

del karyawan1.gaji
karyawan1.tampilkan_profil()
