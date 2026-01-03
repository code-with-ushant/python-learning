class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
         
      return vector(self.x + other.x,self.y+other.y,self.z+other.z)
      
    def __mul__(self,other):
     return self.x * other.x + self.y * other.y + self.z * other.z
    def __str__(self):
      return f"vector ({self.x}x,{self.y}y,{self.z}z)"
    

v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(4,5,6)
print(v1 + v2)
print(v1.__add__(v2))
print(v1*v2)
print(v2+v3)
print(v2*v3)