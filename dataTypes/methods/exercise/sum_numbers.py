
def sum_numbers(*args:tuple) -> int :
    counter:int = 0
    for a in args:
         counter += a

    return counter        

result1 :int = sum_numbers(5,10,15)
result2:int = sum_numbers(7 ,3 ,2 ,1 ,9)
result3:int = sum_numbers()
print(result1)
print(result2)
print(result3)