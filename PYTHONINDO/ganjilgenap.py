def ganjilgenap(bil):
    if bil % 2 == 0:
        return "genap"
    else:
        return "ganjil"

bil = int(input("bilangan : "))
print(bil," adalah bilangan ", ganjilgenap(bil))

print("{0} adalah bilangan {1}".format(bil, ganjilgenap(bil)))