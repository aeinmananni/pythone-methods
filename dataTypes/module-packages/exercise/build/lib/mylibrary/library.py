

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self,title:str,author:str):
        self.books.append({"title":title,"author":author})
        print("Created Books Compeleted Success Fully!")
    
    def remove_book(self,title:str):
        for book in self.books:
            if book["title"].lower() == title.lower():
                 self.books.remove(book)
                 print (f"{title} book Remove Success fully")
 
    
    def search_book(self,title:str):
        for book in self.books:
            book["title"].lower() == title.lower()
            print(f"📖 find book {book["title"]}-{book["author"]}")
    
    def show_books(self):
        if not self.books:
            print("is not find Book!")

        else :
            print("Books list : ")
            for book in self.books:
                print(f" - {book['title']} نوشته‌ی {book['author']}")
