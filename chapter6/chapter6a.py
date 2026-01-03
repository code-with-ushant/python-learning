marks1=int(input("english marks 1: "))
marks2=int(input("economic marks 2: "))
marks3=int(input("computer marks 3: "))
marks4=int(input("nepali marks 4: "))
marks5=int(input("samjik marks 5: "))
marks6=int(input("account marks 6: "))

total_percentage = (marks1+marks2+marks3+marks4+marks5+marks6)/6
if(total_percentage>=40 and marks1>35 and marks2>35 and marks3 >35 and marks4>35 and marks5>35
  and marks6>35):
    print("you are pass",total_percentage,"%")
    print(" your gpa : ",total_percentage/25)
else:
    print("you are fail! better luck next time.",total_percentage,"%")
    print("no gpa")