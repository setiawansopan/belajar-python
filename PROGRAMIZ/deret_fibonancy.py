nterms = int(input('input jumlah deret : '))

n1,n2 = 0,1
count = 0

if nterms <= 0 :
    print('masukkan bilangan positif')
elif nterms == 1:
    print('deret fibonancy',nterms,':')
    print(n1)
else:
    print('deret fibonancy : ')
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1