def perkalian_dari(bil):
    def kali(x):
        return x * bil
    return kali

perkalian3 = perkalian_dari(3)
perkalian5 = perkalian_dari(5)

print(perkalian3(9))
print(perkalian5(5))