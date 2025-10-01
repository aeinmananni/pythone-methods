

def pick_evens(*args:tuple) -> list[int]:
    evens:list[int] = []
    for a in args:
        if a % 2 == 0:
            evens.append(a)
    return evens

result1 = pick_evens(1 ,2 ,3, 4 ,5, 6)
result2 = pick_evens(7 ,13, 19, 21)
print("Result 1: " ,result1)        
print("Result 2: " ,result2)        
