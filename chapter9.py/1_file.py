# with open("ushant.txt") as f:
f = open("file.txt","w")
c="hi i am second ushant"
f.write(c)
f.close()
f = open("file.txt","r")

content = f.read()
if("ushant" in content):
    print("it is about ushant or ushant is present herer !")
else:
    print("this word is not available")

print(content)
f.close()