# متد ها
# توابع
# توی برنامه نویسی پایتون تقریبا همه چیز ابجکت است
# متد : فانکشنی که روی چیزی صدا زده میشود

def Hello_world():
    print("Hello Ayin")

Hello_world();    

print("------------------------")


def sum( a ,  b):
    return a + b;

score = sum(3,4);

print(score)

print("------------------------")

def sendMessage(message:str):
    for _ in range(3):
       print(f"Your Gooding is beutifull! your Message is : {message}")

sendMessage("Im rich boy!")


print("------------------------")





def loop_print(message:str,n:int):
      for _ in range(n):
          print(f"send {message} completed SuccessFully")
      
loop_print("Hello Ayin !",2)      


print("------------------------")
def sum_with_array(res:4):
    result:list[str] = []
    for _ in range(res):
         result.append("MESSAGE")

    return result
       
   
MY_MESSAGE = sum_with_array(10)   
print(MY_MESSAGE)

print("------------------------")

def response_score(score:int):
    result:str=""
    for _ in range(score):
        result += " , Hello Message"
    return result    

response = response_score(3)

print(response)
print("------------------------")


def how_match_character(text:str,char:str):
    counter:int = 0;
    for i in text:
        if i == char:
            counter+=1
    return counter



how_match = how_match_character("How Are you my name is ayin mannani im 28 years old","n")    
print(how_match)
        
print("------------------------")

def returns_any_range(name:str, n:int=1):
    result:str=""
    for i in range(n):
        result += f" , {name}"
    return result

returns_function_result = returns_any_range("Ayin")

print(returns_function_result)

print("------------------------")

def Tavan(number:int,t:int=2):
    result:int = 1
    for _ in range(t):
        result *= number
    return result    

result_tavan_functions = Tavan(2)
print("Tavan : ", result_tavan_functions);