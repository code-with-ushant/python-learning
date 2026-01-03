import random 

def store(s):
    
    with open("score.txt","w") as f:
        f.write(s)
print("plaing game>>>>>>>")
score = random.randint(1,50)
print(f"your score is {score}")


with open("score.txt") as fl:
    f=fl.read()
    if(f==""):
     with open("score.txt","w") as f:
        f.write("0")
    elif(int(f)< score):
     store(str(score))
     print("you make a high score !")