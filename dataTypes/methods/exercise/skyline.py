def skyline(*args:tuple) -> int :
    if not args:
        return 0
    return max(args)

result1 :int = skyline(3 ,7 ,15, 2 ,9)
result2:int = skyline(1 ,1 ,1 ,1)
result3:int = skyline(0)
print("Result 1 : ", result1)
print("Result 2 : ", result2)
print("Result 3 : ", result3)