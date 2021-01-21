angka = [5,4,6,3,7,2,8,6,7,5,8]

jumlah = 0
rata = 0

#loop
for each in angka:
    jumlah = jumlah + each

rata = jumlah / len(angka)
print("jumlah : ",jumlah)
print("rata : ", rata)