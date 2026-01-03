l=["ushant","suman","ayush","tushar","amit","aditya"]

for name in l:
    if (name.startswith("a")):
        print(f"hi {name} .")

n=int(input("Enter a number :"))
for i in range (2,n):
    if(n%i==0):
        print("it is not a prime number.")
        break
else:
        print(f"{n} is a prime number")

# find sum 
a=int(input("Enter a number :"))
i=0
sum=0
while(i<a):
    
    sum=sum+(a-i)
    i = i+1

print(f"sum of this number is {sum}")   
