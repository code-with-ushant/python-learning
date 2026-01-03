#make a calss 2d vector and use it to creat another class representing a 3 d vector.

class dvector2d:
    def __init__(self,a,b):
        self.a=a
        self.b=b

        pass
    def show(self):
        print(f"the vector is {self.a}a + {self.b}b")
class dvector3d(dvector2d):
    
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
        pass
    def show(self):
        print(f"the vector is a{self.a }+b{ self.b}+c{self.c}")

a= dvector2d(2,3)
a.show()
b= dvector3d(2,3,4)
b.show()