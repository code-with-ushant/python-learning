
n=int(input("Enter the number :"))
table = [i*n  for i in range(1,11)]
print(table)
with open("table.txt","a") as f:

    f.write(f"Table of {n} is {str(table) } \n")
  
    print("sucessfullly transfer to table.txt")
with open("table.txt","r") as f1:
    print(f1.read())
