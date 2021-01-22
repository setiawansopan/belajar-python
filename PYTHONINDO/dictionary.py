orang = {'nama':'arfinda', 'usia':24}
print(orang['nama'])
print(orang.get('usia'))
#update data
orang['usia'] = 25
print(orang)
#insert data
orang['alamat'] = 'magelang'
print(orang)
#hapus
print(orang.pop('alamat'))
print(orang.popitem())

#hapus semua
del orang
#print(orang) ini error karena dictionary sudah dihapus