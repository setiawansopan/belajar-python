import math

def isperfectsquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isfibonacci(n):
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4)

for i in range(1, 11):
    if(isfibonacci(i) == True):
        print(i,'is fibonacci number')
    else:
        print(i,'is not fibonacci number')