mulai = 1
selesai = 100

for i in range(mulai, selesai+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)