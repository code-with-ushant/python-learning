#find factoral of any number 
# a= int(input("Enter the number"))
# factoral = 1
# for i in range(1,a+1):
#     if (a==0 or a==1):
#         print(factoral)
#     else:
#         factoral = factoral *i
   
     
# # print(factoral)
# n=int(input("Enter the number : "))
# for i in range(1,(n+1)):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1))
    
    
# n=int(input("Enter the number : "))
# for i in range(1,(n+1)):
   
#     print("*"*i)
    
  # * * *
    
n=int(input("Enter the number : "))
for i in range(1,(n+1)):
    if(i==1 or i==n):
        print("*"*n)
    else:
     print("*",end="")
     print(" "*(n-2),end="")
     print("*")
    