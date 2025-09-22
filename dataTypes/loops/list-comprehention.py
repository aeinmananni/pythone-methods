
# list-comprehention : اجازه میدهند محتوای یک لیست رو تبدیل به لیست جدید کنیم

oldList = [2,3,4,5,6]
newList = []

for i in oldList:
    newList.append(i * 2)

print("New List Version1: " , newList)
print("--------------------------------------")
# نمونه دیگری که میتوانیم این کد را بازنویسی کنیم

newlist2 = [x * 2 for x in oldList]


print("New List Version2 : " , newList)
print("--------------------------------------")

a = 5
result = 'Fard' if a % 2 != 0 else "Zog"


print("Result : " , result)
print("--------------------------------------")

result2 = [n for n in oldList if n % 2 ==0]
print("Result 2 " , result2)

print("--------------------------------------")

result3=['zoj' if n % 2 == 0 else "fard" for n in oldList]
print("Result3 : " , result3)


print("--------------------------------------")

RESULT_HOPE = ['HOP' if n % 5 == 0 else n for n in range(1,30)]

print(RESULT_HOPE)