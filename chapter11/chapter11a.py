class animal:
    pass
class pets(animal):
    pass
class dog(pets):
    @staticmethod # it is used for not taking argument for function
    def bark():
        print("bhau bhau")
    pass
d=dog()# d is a object which is made from class dog
d.bark()# in this bark function were call from d object which is mad of dog class