a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
#gabungan
print(a | b)
print(a.union(b))
#irisan
print(a & b)
print(a.intersection(b))
#diference
print(a -b)
print(a.difference(b))
print(b.difference(a))
#komplemen
print(a ^ b)
print(a.symmetric_difference(b))
print(b ^ a)
print(b.symmetric_difference(a))
