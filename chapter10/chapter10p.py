class programmer:
    company = "microsoft"
    def __init__(self,name, salary,pin): # init helps to run code one time in every sutuation
        self.name = name
        self.salary = salary
        self.pin = pin
        pass
p1= programmer("ushant","2000000","765")
p2= programmer("harry","200000","065")

print(p1.name,p1.company,p1.pin,p1.salary)
print(p2.name,p2.company,p2.pin,p2.salary)
