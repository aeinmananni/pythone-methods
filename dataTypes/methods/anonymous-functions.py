def tavan_2(x:int) -> int:
    return x ** 2
numbers:list[int] = [1,2,3,4,5,6]

for i in range(len(numbers)):
    numbers[i] = tavan_2(numbers[i])

print("with For loop : " ,numbers)    

print("-----------------")

my_list:list[int] = [1,3,5,7]

Numbers:list[int] = []
for i in my_list:
    Numbers.append(tavan_2(i))


print("ssss : " , Numbers)    

print("-----------------")

count_score:list[int] = [1,2,3,4,5,6]

Counter_Score_Lambda = map( lambda x:x,count_score)

for i in Counter_Score_Lambda:
    print("Counter Score : " , i)

print("---------------------------------")

Score:list[int] = [5.65,13.65,54,12,1,3,5,7]

Result_score = filter(lambda x:x != int(x),Score)
print(list(Result_score))
print("---------------------------------")


firstName:list[str] = ["Hadi","Rohallah","Majid jan","Ali"]
Result_firstName = list(filter(lambda f:len(f) <= 3,firstName))

print("Filters : " , Result_firstName)

multyply:int = lambda x , y : x * y
print(multyply(3,4))