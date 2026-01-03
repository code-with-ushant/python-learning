bword =["bad","fuck","bitch","noob","suck","dick"]
sword =["subscribe","like","follow","click","earn"]

c = " hi my name is ushant giri follow me to earn lotes of money subscribe me noob suck my dick"
with open("2file.txt","w") as f:
 f.write(c)
with open("2file.txt") as f:
  c = f.read()
for word in bword:
   
   c = c.replace(word,"#"*len(word))
# elif(c in sword):
#     print("it is a spam !")
# else:
#     print("this message is good !")
with open("2file.txt","w") as f:
  f.write(c)

with  open ("2file.txt") as f:
  c= f.read()
print(c)