import pyttsx3
engine = pyttsx3.init()
name= input("enter your name :")
age= input("enter your age:")
address= input("enter your address :")
fname= input("enter your father name :")
mname=input("enter your mother name :")
# chose = input("do you have any sibling ? yes or no")
# if(chose== yes ):
bname=input("enter your brother name :")


engine.say(f'''Hi! {name} how are you ? i hope your are fine in the age of {age} . i know that you are child of {fname} and {mname}. how you feel to have a parents like them
           i here that you have a brother too . who is younger than you . whose name is {bname}. i hope you all live happy life in {address} . good bye {name}.''')
engine.runAndWait()