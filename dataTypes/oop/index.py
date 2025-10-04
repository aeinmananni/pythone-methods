
class Person():
    def __init__(self,firstName:str):
        self.firstName = firstName
        print("Object Created !")
    def say_hello(self):
        print("Say Hello")


person1 = Person("Hadi")
print(person1.firstName)
person1.say_hello()

print("---------------")

class Human():
    def __init__(self):
        pass
    def full_name(self):
        return "Im Human"
    
human1 = Human()

print(f">> {human1.full_name()}")


print("--------------------------")

class Car():
    def __init__(self,color:str,price:int,brand:str):
        self.color = color
        self.price = price
        self.brand = brand

    def Message(self):
        return f"my Car Color {self.color} and Price {self.price} => Bard {self.brand}"    
    


Car1:Car = Car(color="Red",price=43210000,brand="BMW")    
Car2:Car = Car(color="Blue",price=3200098,brand="Purch")    

print("Car1 : ", Car1.Message())
print("Car2 : ", Car2.Message())


print("--------------------------")




class Animals():
    def __init__(self):
        pass

    def Eat(self):
        return "Im Animal and I Can Eat!"
    

dolfin:Animals = Animals()

print("Animals : " , dolfin.Eat())

print("--------------------")

class Circle():
    pi:float = 3.1415926
    def __init__(self,r:int):
        self.r = r

    def masahat(self):
        return self.r * self.r * Circle.pi


ci:Circle = Circle(20)
returl :float = ci.masahat()
print("Circluar Msahat : " , returl)
        

class PersonMessage:
    def sey_hello(self):
        return "Hello!"

message = PersonMessage()            

print(message.sey_hello())