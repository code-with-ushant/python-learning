# from functools improt reduce

# using a map function 
l=[1,2,3,4,5]
square = lambda x:x*x
sqlist = map (square , l)#map function take a argument of function and list
print(list(sqlist))

#filter example
def  even(n):
    if(n%2 == 0):
        return True
    return False
onlyeven = filter(even,l)
print(list(onlyeven))

#reduce function take a two data form list to fullfill its function argument and return any one data and store it in list so it requse number of data or value present on list
# sum = lambda a,b: a+b 
# print(reduce(sum,l))