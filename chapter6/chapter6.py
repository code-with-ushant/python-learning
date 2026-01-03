a1= int(input("enter number 1 :"))
a2= int(input("enter number 2 :"))
a3= int(input("enter number 3 :"))
a4= int(input("enter number 4 :"))

if(a1>a2 & a1>a3 & a1>4):
   print(f"{a1} is greatest .")
elif(a2>a3 and a2 >a4):
   print(f"{a2} is greatest.")
elif(a3>a4):
   print(f"{a3} is greatest .")
else:
   print(f"{a4} is greatest .")
