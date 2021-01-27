class Karyawan:
    '''dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1
    
    def tampilkan_jumlah(self):
        print('Total karyawan : ', Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print('Gaji : ', self.gaji)

karyawan1 = Karyawan('arfinda', 5000000)
karyawan2 = Karyawan('umi k', 4000000)
karyawan3 = Karyawan('diah kartika', 3500000)

print('Karyawan.__doc__:', Karyawan.__doc__)
print('Karyawan.__name__:', Karyawan.__name__)
print('Karyawan.__module__:', Karyawan.__module__)
print('Karyawan.__dict__:', Karyawan.__dict__)
print('Karyawan.__bases__:', Karyawan.__bases__)
