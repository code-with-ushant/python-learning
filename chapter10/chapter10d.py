#program to take a ticket of train 
import random
class train :
   def __init__(self,trainno):
      self.trainno = trainno
   def book(self,fr,to):
      print(f"ticket is booked in train number {self.trainno} from {fr} to {to}")
   def getstatus(self):
      print(f"train number {self.trainno} is runing on time")
   def getfare(self,fr,to):
    print(f"ticket fare in train number {self.trainno} from {fr} to {to} is Rs.{random.randint(10,200)}")


t1= train(34343)
t1.book("pakali","labipur")
t1.getfare("pakali","labipur")
t1.getstatus()