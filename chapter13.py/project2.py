#wap toinput name,marks and phome number of a student of format it useing the format function like below:
name = input("enter the name :")
marks = int(input("enter the marks :"))
pnumber = int(input("enter the phone number :"))

info = "The name of the student is {},his marks are {} and  phone number is {} " .format(name,marks,pnumber)
print(info)