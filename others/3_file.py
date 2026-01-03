c = '''hi ushnat
hi python
hi coder
hi programer
what are you doing
'''
with open("3file.txt","w") as f:
    f.write(c)
with open ("3file.txt") as f:
    lines = f.readlines()
  
    lineno=0
    c = "coder"
    for i in lines:
       
      if(c in i):
         
        print(f"{i} is present in {lineno+1} number ")
        break
      lineno = lineno + 1
    else:
       print("didn't found !")

    