def faktorial(x):
    if x == 1:
        return 1
    else:
        return(x * faktorial(x-1))

bil = int(input('bil : '))
print('Faktorial dari ',bil,'adalah ', faktorial(bil))