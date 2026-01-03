#calculator 
class calculator:
    # def __init__(self,num):
    #     self.square = (num*num)
    #     self.cube = (num**3)
    #     self.square_root = (num**1/2)
    #     pass
    def __init__(self,num):
         self.num=num
    def square(self):
          print(self.num*self.num)
    def cube(self):
          print(self.num**3)
    def square_root(self):
           print(self.num**1/2)
    @staticmethod   # this is used whne you dont want self in any function you are making because in any class if you are making any function they you have to call self
    def hello():
          print("hello ,world!")
c = calculator(3)

c.square()