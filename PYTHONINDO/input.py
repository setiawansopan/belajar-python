def segi3(alas, tinggi):
    luas = (alas * tinggi)/2
    return luas

a = int(input('alas : '))
t = int(input('tinggi : '))
print('luas : ', segi3(a,t))