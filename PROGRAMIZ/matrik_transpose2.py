x = [[12,7], 
     [4,5], 
     [3,8]]

hasil = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

for h in hasil:
    print(h)