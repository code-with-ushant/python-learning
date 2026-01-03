try: #try is used for trying some things which can be worng and cause error but it help to procted form crash and just return message form execption 
 with  open("1.txt","r") as f1 :
       print(f1.read())
except Exception as e:# this help to stop crash and get  erro message only and contunue other programs
    print(e)
try:# 
 with open("2.txt","r") as f2 :
       print(f2.read())
except Exception as e:
    print(e)
try:
 with open ("3.txt","r") as f3 :
       print(f3.read())
except Exception as e:
    print(e)
print("Thank you !")
print(__name__)