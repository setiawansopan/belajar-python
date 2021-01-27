class Induk:
    def my_method(self):
        print('memanggil metode induk')
    
class Anak:
    def my_method(self):
        print('memanggil metode anak')

c = Anak()
c.my_method()

i = Induk()
i.my_method()
Induk().my_method()