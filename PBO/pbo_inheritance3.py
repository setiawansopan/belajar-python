class Orang:
    def __init__(self, nama, kelamin):
        self.nama = nama
        self.kelamin = kelamin
    
    def info(self):
        print('nama : {}, \njenis kelamin : {}'.format(self.nama, self.kelamin))

class Pelajar(Orang):
    pass

Joko = Pelajar('Joko susanto', 'laki-laki')

Joko.info()