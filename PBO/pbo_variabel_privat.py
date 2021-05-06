# encapsulation
class siswa:
    # konstruktor
    def __init__(self, nis, nama, kelamin):
        self.__nis = nis
        self.__nama = nama
        self.__kelamin = kelamin
    #buat decorator
    @property
    def nis(self):
        pass

    # getter
    @nis.getter
    def nis(self):
        return self.__nis

    # setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis 


# instansiasi objek
susi = siswa("12345", "susilowati", "Perempuan") 

print("Nis : ", susi.nis)
susi.nis = "54321"
print("New Nis : ", susi.nis)
print("Update Sukses")




