#import modul
import fibo

#pemanggilan fungsi pertama
print(fibo.fib(100))

#pemanggilan fungsi ke dua
print(fibo.fib2(100))
print()

#pemanggilan fungsi dengan nama lokal
fib = fibo.fib
print(fib(100))
print()

#print isi fibo
print(dir(fibo))