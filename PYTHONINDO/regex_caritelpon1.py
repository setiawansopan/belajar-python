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

print('021 8229311 dalah nomor telepon?')
print(is_phone_number('021 8229311'))
print('Hello Hello adalah nomor telepon?')
print(is_phone_number('Hello Hello'))