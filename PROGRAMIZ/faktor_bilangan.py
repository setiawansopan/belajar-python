def print_factors(x):
    print('faktor dari ',x,'adalah :')
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

num = 320

print_factors(num)