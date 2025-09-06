firstName = "ali"
lastName="rahimi"

print(firstName + lastName)

print("-----------------------------------")

print("Hello I'm Very Goods")

print("-----------------------------------")

# میتوانیم ما لیست با رشته ها برخورد کنیم

message = "this is my message"
print('MESSAEG : ',message[3])
print("-----------------------------------")
# حالا میخواهیم اسلایس را انجام دهیم مثال میخواهیم بگوییم از ایندکس 1 تا 4 رو برای ما کپی بگیر
slice1 = message[0:4]

print(slice1)
print("-----------------------------------")
# زمانی که بخواهیم اعداد را منفی بدهیم از انتهای رشته برای ما کلمات را برمیگرداند
variable1 = "my name is ayin"
slice2 = variable1[-4] 
# => output : a
print(slice2)

print("-----------------------------------")
# میتوانیم مشخص کنیم زمانی که میخواهد اسلایس را انجام دهد چند تا چندتا حرکت کند

sliceMessage  = "this message can be slice!"
sliced = sliceMessage[1:4:2]
print(sliced)

print("-----------------------------------")

# میتوانیم اعداد منفی را نیز در اسلایس لحاظ کنیم

sliceMessage2 = "123456789"
sliceNumber1 = sliceMessage2[1:6]
sliceNumber2 = sliceMessage2[1:6:2]
sliceNumber3 = sliceMessage2[1:-1]
print(sliceNumber1)
print(sliceNumber2)
print(sliceNumber3)
# بگیر تا اخر n  خب حالا  برای مثال میخواهیم بگوییم از 
sliceNumber4 = sliceMessage2[3:]
print(sliceNumber4)

# خب حالا برای مثال میخواهیم از ته برای ما اعداد را نمایش دهد به نوعی اعداد ریورس میکند
sliceNumber5 = sliceMessage2[::-1]
print(sliceNumber5)

#  بزنیم و یک تکست را بنویسم enter میتوانیم در چند خط 
print("-----------------------------------")

enterMessageSchema = """ this
is
my
 message
 Enter
 Schema

"""

print(enterMessageSchema)
# در زبان برنامه نویسی بک اسلش برای نمایش دادن کارکتر های خاص بکار میرود
# 
# \n  بکار میرد enter  برای  
# مانمیتوانیم قسمتی از یک استرینگ رو توی پایتون تغییر دهیم
# مثال : 
name ="aliReza"
# name[0] = 'A' 
# به این صورت نمیتوانیم مقداری از ان را تغییر دهیم

# خب یکی از راه هایی که میتوانیماین کارکتر را تغییر دهیم
name = "A" + name[1:]
index=3
new_char="r"
name = name[0:index] + new_char + name[index + 1:]
print(name)

print(name)