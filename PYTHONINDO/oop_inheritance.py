class Induk:
    parent_attr = 100

    def __init__(self):
        print('memanggil konstruktor induk')

    def parent_method(self):
        print('memanggil metode induk')
    
    def set_attr(Self, attr):
        Induk.parent_attr = attr
    
    def get_attr(self):
        print('Atribut induk : ', Induk.parent_attr)

class Anak(Induk):
    def __init__(self):
        print('memanggil konstruktor anak')
    
    def child_method(self):
        print('memanggil metode anak')

c = Anak()
c.child_method()

c.parent_method()
c.set_attr(200)
c.get_attr()

