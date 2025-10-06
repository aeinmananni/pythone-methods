
#  Built-in exceptopns-pythone میتوانیم سرچ کنیم 




try:
    print("result is test")

except:
    print("Except New Error")    

print("--------------------------")

def divise(a:int,b:int) -> int :
    try:
        return a / b
    
    except ZeroDivisionError:
        print("b can not be 0")
        return False
    except Exception as error:
        print(f"Another error: e = {error} ")
        return False

    


print(divise(1,3))
print(divise(3,0))
print(divise("a",0))

print("----------------------------")


def finding_file_path(path:str) -> bool:
    try:
        open(path)
    except FileNotFoundError:
        print("file dose not Exsist")
        return False
    except Exception as e:      
        print(f"Another Error : {e}")  
        return False
    

finding_file_path("/path/ayin")    

print("-------------------------------")


def Sumoration(a:int,b:int)-> int :

    try:
        r = a / b
    except Exception as error:
        print(f"Aanother Error e = {error}")
        r = 0
    else:
         return r

    finally:
        return r




print(Sumoration(2,4))
    
    