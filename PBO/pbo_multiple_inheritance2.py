class A:
    def infoA(self):
        print("Ini adalah kelas A")

class B:
    def infoB(self):
        print("Ini adalah kelas B")

class C(A, B):
    pass

D = C()
D.infoA()
D.infoB()