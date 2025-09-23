
# محدوده range(10)
# زمانی که داریم همچین چیزی را مینویسیم در واقع میگویم محدوده
# اعداد از 0 تا 9 را برای من نمایش بده 
for i in range(10):
    print("Range : " , i)
# output => 
            # Range :  0
            # Range :  1
            # Range :  2
            # Range :  3
            # Range :  4
            # Range :  5
            # Range :  6
            # Range :  7
            # Range :  8
            # Range :  9
print("-------------------------");           


# خب حالا فرض کنیم میخواهیم جدول ضرب درست کنیم  
# هم مشخص کنیمend نکته دیگری وجود دارد میتوانیم برای دستور پرینت 
for i in range(6):
    for j in range(6):
        print( i * j , end="\t")
    print(" ")
# output => 
# 0       0       0       0       0       0        
# 0       1       2       3       4       5        
# 0       2       4       6       8       10       
# 0       3       6       9       12      15       
# 0       4       8       12      16      20       
# 0       5       10      15      20      25  


print("-------------------------");              


for i in range(10):
    print(i , end=" ")

# 0 1 2 3 4 5 6 7 8 9
print()
print("-------------------------");   
# میتوانیم تایین کنیم از چه مقدار تا چه مقداری را میخواهیم

for i in range(1,21):
    print(i)
    # output =>
               # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

print("-------------------------");   

# خب حالا میخواهیم بگوییم از چه عددی تا چه عددی و چند تا چند تا پیش بره

for i in range(10,31,5):
    print(i)

    # output =>
                # 10
                # 15
                # 20
                # 25
                # 30    
print("-------------------------");   

# خب حالا میتونیم این کار رو به صورت برعکس هم انجام بدیم

for i in range(10,0,-1):
    print(i)
# output =>    
            # 10
            # 9
            # 8
            # 7
            # 6
            # 5
            # 4
            # 3
            # 2
            # 1 
print("-----------------------enumerate---------------------------");  

# عددی کردن 
#  داریم و میخوایم عددیش کنیم list , tuple, string فرض کنیم 
# و میخوایم بگیم حرف اول یا دوم یا سومش چیه


firstName = "mohamad"
for i in range(len(firstName)):
    print("Len " , i , firstName[i])

# output => 
            # Len  0 m
            # Len  1 o
            # Len  2 h
            # Len  3 a
            # Len  4 m
            # Len  5 a
            # Len  6 d

print("---------------------------")


personal_firstName:list[str] = ["ali","hossine","reza","sara"]           

for i in range(len(personal_firstName)):
    print(i,personal_firstName[i])
# output =>
            # 0 ali
            # 1 hossine
            # 2 reza
            # 3 sara
print("---------------------------")

numbers:tuple[int] = (1,2,3,4,5,6,7,8,9,10)
result =enumerate(numbers)

for index,value in result:
    print (f"{index}-{value}")
# output =>
            # 0-1
            # 1-2
            # 2-3
            # 3-4
            # 4-5
            # 5-6
            # 6-7
            # 7-8
            # 8-9
            # 9-10
print("-----------------------zip---------------------------");              
# باعث وصل شدن مقدایر به یکدیگر میشود

firstNames:list[str] =["Ali","Sara","Mehdi"]
lastNames:list[str] =["Rahimi","Ebrahimi","Mannani"]
ages:list[int] = [32,24,28]

for result in zip(firstNames,lastNames,ages):
    print("Result Zip Model : ",result)

# output =>
            # Result Zip Model :  ('Ali', 'Rahimi', 32)
            # Result Zip Model :  ('Sara', 'Ebrahimi', 24)
            # Result Zip Model :  ('Mehdi', 'Mannani', 28)  
            # 
            # 
            #   
print("-----------------------in---------------------------");  
#  string, tuple , list برای برسی وجود یک عنصر در 

languege:list[str] = ["C++","Pythone","Javascript"]

Result_Model:bool = "C++" in languege

print("In Check : ", Result_Model)

print("--------------")

fullName:str = "Ayin Mannani"
if "Ayin" in fullName:
    print("Yes")
else:print("No")    
print("--------------")

rols:list[str] = ["admin","gest","user"]
users:dict = {
          "admin":{'id':1,'firstName':'rasol','lastName':'javadi'},
          "user":{'id':2,'firstName':'kamal','lastName':'abasi'},
}

for rol in rols:
    if rol in users:
        print(f"id : {users[rol]['id']} isFirstName : {users[rol]['firstName']} is lastName : {users[rol]['lastName']}" )

# output =>
            # id : 1 isFirstName : rasol is lastName : javadi
            # id : 2 isFirstName : kamal is lastName : abasi        

print("--------------------------max-----------------------")

score1:list[int] = [1,43,12,2,3]

print("MAX : " , max(score1))

# output => MAX :  43

print("--------------------------min-----------------------")

score2:list[int] = [1,43,12,2,3]

print("MIN : " , min(score2))

# output => MIN :  1


print("--------------------------from random import randint-----------------------")


# خب حالا برای مثال میخوایم از عدد های رندوم استفاده کنیم
# میخوایم یک عدد تصادفی بین 1 تا 10 بهمون بده 
from random import randint;
rand:int = randint(1,10)
print("Random Numbers : " , rand)

# outptu => Random Numbers :  9
# outptu => Random Numbers :  2
# outptu => Random Numbers :  8
# ....

print("--------------------------input-----------------------")

message = input("please send your message : ")
print(message)

# output =>
# please send your message : hi ali how are you
# hi ali how are you

print('-------------')

RESPOSE:int = 6
i = input("Give Me your Numbers Please : ")
if int(i) == RESPOSE:
    print("Yes Approve 🥳") 
else:
    print(f"no my Number is {RESPOSE} 😣")    

# output => 
# Yes Approve 🥳  OR  no my Number is 6 😣