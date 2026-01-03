#print star partern using function recorson..
n=5
def partern(n):
    if(n==0):
        return 0
    print("*"*n)
    partern(n-1)

print(partern(4))