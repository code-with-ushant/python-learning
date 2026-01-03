# class and object
class student:
    name = ""
    grade = ""
    rollno =""

student1 = student()

student1.name= input("enter the name :")
student1.grade= input("enter the grade :")
student1.rollno= input("enter the rollno :")

print(f"Name :{student1.name}\n Class :{student1.grade}\n Roll no :{student1.rollno}")