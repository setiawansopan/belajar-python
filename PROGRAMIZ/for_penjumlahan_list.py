numbers = [4,5,7,6,8,9,3,2,5,4,6]

def jumlah(lst):
    sum = 0
    for bil in lst:
        sum = sum + bil
    return sum

def rata(lst):
    return sum(lst)/len(lst)

print('jumlah semua data dalam list adalah : ', jumlah(numbers))
print('rata-rata bilangan dalam list adalah : ', rata(numbers))