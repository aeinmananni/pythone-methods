
from mylibrary import library

def main():
    lib:library.Library = library.Library()
    while True:
        print("\n --- سیستم مدیریت کتابخانه ---")
        print("1. افزودن کتاب")
        print("2. حذف کتاب")
        print("3. جستجوی کتاب")
        print("4. نمایش همه‌ی کتاب‌ها")
        print("5. خروج")

        choice = input("گزینه مورد نظر را انتخاب کنید ->")

        if choice == "1":
            title = input('عنوان کتاب : ')
            author = input("نویسنده : ")
            lib.add_book(title=title,author=author)
        elif choice == "2":
             title = input("عنوان کتاب برای حذف : ")
             lib.remove_book(title=title)
        elif choice == "3":
            searchTitle = input("جستجوی کتاب مورد نظر : ")         
            lib.search_book(title=searchTitle)
        elif choice == "4":
            lib.show_books()
        elif choice == "5":
            print("final!")
            break;
        else:
            print("گزینه نامعتبر !!")    
                

if __name__ == "__main__":

  main()