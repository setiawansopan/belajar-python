num = 16

if num < 0:
    print('masukkan bilangan positif : ')
else:
    sum = 0

    while(num > 0):
        sum += num
        num -= 1
    print('jumlah : ',sum)