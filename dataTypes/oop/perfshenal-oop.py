
class Book:
    def __init__(self,name:str,page:int):
         self.name = name
         self.pages = page

    def open(self):
         return f"opend {self.name} which has {self.pages} pages"      
    

b1:Book = Book(name="C Progaraming" ,page=254)
b2:Book = Book(name="Defi Progaraming" ,page=543)

print(f"Book 1 {b1.open()}")
print(f"Book 2 {b2.open()}")

print("--------------Inhritense---------------")

class Darsi(Book):
     def __init__(self, reshte:str,paye:str,name:str,page):
          super().__init__(name,page)
          self.reshte = reshte
          self.paye = paye
          

     def open(self):
          return f"{super().open() } and Reshte = {self.reshte} and paye = {self.paye}"     
          
D1:Darsi = Darsi(reshte="Tajrobi",paye="Tajrobi",name="Oroloji",page=543)          

print("DDDDD : " ,D1.open())

print("----------Polymorfiseme-----------")

class Runner:
     def __init__(self,name:str):
          self.name = name


     def action(self):
          return f"Action to Run {self.name}"     
     
hadis:Runner = Runner(name = "Hadis")

print("Call Runner Class : " , hadis.action())


class Cyclist:
     def __init__(self,name:str):
          self.name =name

     def action(self):
          return f"Cyclist Run Action {self.name}"     
     


alireza:Cyclist = Cyclist(name="Tavasoli")

print("Cyclist Class : " , alireza.action())

for MyAction in [hadis,alireza]:
     print(MyAction.action())


print("------------abstraction---------------")



class Human:
     def __init__(self):
          pass
     
     def jump(self):
          raise NotImplementedError("implement the Junp Please")

class Progarammer(Human):
     def jump(self):
          return "Jump !!!!"

ayin = Progarammer()

print("Send Message : ",ayin.jump())