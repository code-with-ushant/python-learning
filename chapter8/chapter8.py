# #function to find greatest number among three
# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# c=int(input("enter the number :"))

# def find(a,b,c):
#     if(a >b and a>c):
#        return a
#     elif(b>c):
#         return b
#     else:
#         return c
    
# print("the greatest number among them is ", find(a,b,c))

# #function to convert c to f
# def converter(c):
#   return 9*(c/5)+32

# c=int(input("enter the temperture in c :"))
# print(round(converter(c),2))
# #function to find sum

def sum(n):
   if(n==1):
      return 1
   else:
    return n+sum(n-1)

print(sum(5))