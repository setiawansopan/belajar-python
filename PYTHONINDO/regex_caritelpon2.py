#ini fungsi biasa tanpa menggunakan regex
def is_phone_number(text):
    if len(text) != 11:
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != ' ':
            return False
    for i in range(4, 11):
        if not text[i].isdecimal():
            return False
    return True

pesan = 'Panggil saya di nomor 061 9895424 besok. Kalau sore bisa hubungi kantor saya di 061 8574930'

for i in range(len(pesan)):
    text = pesan[i:i+11]
    if is_phone_number(text):
        print('Nomor telepon ditemukan : ', text)
print('selesai')