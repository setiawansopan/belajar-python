my_list = [1,2,3,4,5,6,7,8,9,10]
list_ganjil = list(filter(lambda x: x%2 != 0, my_list))
list_genap  = list(filter(lambda x: x%2 == 0, my_list))
kuadrat = list(map(lambda x: x*x, my_list))

print(list_ganjil)
print(list_genap)
print(kuadrat)