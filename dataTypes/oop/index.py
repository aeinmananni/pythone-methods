
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
