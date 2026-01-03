name = input("Enter your name : ")
# age =input("enter your age :")
date= "20 september 2030"

# print(f"Good afternoon {name}. your age is {age}")
# print(f"Dear {name}\nYou are selected!\n{date}")
letter ='''Dear <name>,\n\tYou are selected!
           <date>'''
print(letter.replace("<name>",name).replace("<date>",date))
print(name.replace("giri","don"))
# name=name.replace("giri","don")
print(name)