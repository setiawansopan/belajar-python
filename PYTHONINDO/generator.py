def my_gen():
    n = 1
    print('ini pertama')
    yield n

    n += 1
    print('ini kedua')
    yield n

    n += 1
    print('ini terahir')
    yield n

#a = my_gen()
#next(a)
#next(a)
#next(a)

for item in my_gen():
    print(item)