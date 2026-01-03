#wap to print third fith and seventh element form a list using enumerate function.
l =[1,2,3,4,5,6,7]

for i,item in enumerate(l):#enumerate helps us to run index and item in same time and hlep to find index and item in a same time
    if i == 2 or i==4 or i==6 :
        print(item)