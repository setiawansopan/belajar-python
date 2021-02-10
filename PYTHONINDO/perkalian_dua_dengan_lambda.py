terms = 10

result = list(map(lambda x: 2 ** x, range(terms)))

print('Total terms adalah : ',terms)
for i in range(terms):
    print('2 pangkat ',i,'adalah ',result[i])