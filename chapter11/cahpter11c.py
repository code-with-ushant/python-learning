class complex:
    def __init__(self,r,i):#for defining or inserting data in class of object
        self.r= r
        self.i = i
    def __add__(self,c2):#it helps to add complex number from diffrent object
            return complex(self.r+c2.r ,self.i + c2.i)
    def __mul__(self,c2):# same as addition it helps to multiply complex number
            return complex(self.r*c2.r ,self.i *c2.i)
    def __str__(self):# to return final value
            return f"{self.r} + {self.i}i"

     
 
    c1 = complex(1,2)
    c2 = complex(3,4)
    print(c1+c2)
    # print(c1.__add__(c2))
   