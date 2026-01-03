#creat a class "employee" and add salary and increament properties to it.
class employee:
    salary =200
    increament = 10
    @property
    def salaryafterincrement(self):
        return (self.salary +( self.salary * (self.increament/100)))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increament = ((salary/self.salary)-1)*100
    pass

ram = employee()
print(ram.salary)

print("salary in increase by 20% ",ram.salaryafterincrement)
ram.salaryafterincrement=300
print(ram.increament)