num = int(input('masukkan nomor : '))

sum = 0
pangkat = len(str(num))

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** pangkat
    temp //=10

if num == sum:
    print(num,'adalah nomor amstrong')
else:
    print(num,'bukan nomor amstrong')