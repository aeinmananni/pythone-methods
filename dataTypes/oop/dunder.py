
class Book():
    def __init__(self,name:str,page:int):
        self.name = name
        self.pages = page


    def open(self):
        return f"opend the {self.name} which has {self.pages} pages"     
    # dunder methods : برای تعریف کردن متد های خاص برای یک کلاس استفاده میشوند
    def __len__(self): 
        return self.pages
      
    def __str__(self):
         result = f"{self.name}-{self.pages}"
         return result
    
    def __del__(self):
        print(f"Oh the {self.name} book is vanishing!") 

    

book1:Book = Book(name="Bok1",page=321)

print(book1.open())
print('Len Mthods : ',len(book1))
print("String Reverse Methods1 : ", str(book1))
print("String Reverse Methods2 : ", book1)
del book1
