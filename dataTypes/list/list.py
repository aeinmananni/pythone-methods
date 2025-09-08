# لیست ها یا ارایه ها []
# کارهایی را که میخواهیم انجام دهیم درون یک لیست قرار میدهیم تا بتوانیم با اجزا ان کار کنیم
# مثال :
# زمانی که بگوییم که فایلی داریم که یک عالمه خط درد و میخواهیم ان را بخوانیم
# میتوانیم بگوییم خط به خط را تبدیل به یک لیست کن و ان را خط به خط بخوان

numbers  = [0,1,2,3,4,5]
print(f" Index : {numbers[0]}")
print(numbers)

print("------------------------------")

names =["ali","hadi","sina","davood"]
print(f" my name is : {names[0]}")
print(names)

print("------------------------------")

# خب حالا برای مثال میخواهیم از یک ایندکسی تا یک ایندکس دیگری را بدست اوریم

full_names=["ehsan nabavi",'ayin mannani','alireza karimi','sohile poAHmadi']
# از یایندکس 0 تا قبل از 2را میدهد
print(full_names[0:2]) 
# از ابتدا تا ایندکس 3 را میخواهیم
print(full_names[:3]) 
# میتوانیم بگوییم از دومی تا اخر
print(full_names[2:]) 

# میتوانیم ار هر نوعی که میخواهیم درون ارایه استفده کنیم

print("------------------------------")

LENGTH_VALUE = [1,2,3,4,5,6,7,8,9]
print(f"LENGTH : {len(LENGTH_VALUE)}")

print("------------------------------")
# میتوانیم لیست هارو باهم دیگه جمع کنیم
SUM1 = ["Happy","Sports","Homes"]
SUM2 =[1,2,3,4,5,]
print(SUM1 + SUM2)
# میتوانیم لیست هارا دوبرابر کنیم
DOUBLE_NUMBERS=[1,2,3]
print(DOUBLE_NUMBERS *  2)
print("------------------------------")
# میتوانیم با قرار دادن دات متد هایی را که برای ارایه میتوانیم استفاده کنیم ببینیم

# میخواهیم بدانیم چه تعدادی از یک عنصر درون لیست داریم
COUNT_NUMBER =[1,1,1,2,3,3,3,3,3,5]
print(COUNT_NUMBER.count(3))
print("------------------------------")

REMOVE_EL = [1,2,3,4,6,6,7]
print(REMOVE_EL.pop())
print(REMOVE_EL)

# میتوانیم لیست های خود را سورت کنیم
SORT_LIST = [1,23,10,9,8,1,2]
NEW_LIST =sorted(SORT_LIST) 
# استفاده کنیم reversed یا میتونیم از  
print(NEW_LIST)

NAMES=["hadi","rasol","sara","maryam"]
NAMES.sort()
print(NAMES)

print("------------------------------")

REMOVE_METHOD = ["HATEF","KOLSOM","ZAHRA","HADIS"]
REMOVE_METHOD.remove("ZAHRA")
print(REMOVE_METHOD)