
firstName="ayin"
lastName="mannani"
print('Hello ' + firstName + ' ' + lastName)

print('------------------------------------------------')

title="Cinema"
exp="i I,Like"
CombindText ="Hello {} {} Very Very Match".format(exp,title)

print(CombindText)
print('------------------------------------------------')
# میتوانیم در این حالت مشخص کنیم چه ایندکسی نمایش داده شود

text1="Hello"
text2="Ali"
text3="Im 28 yreas old"
combind2 = "{1} {0} {2}".format(text1,text2,text3)
print(combind2)

print('------------------------------------------------')

text1="Hello"
text2="mohamad"
text3="Im 31 yreas old"
combind3 = "{name} {message} {exp}".format(message=text1,name=text2,exp=text3)
print(combind3)

print('------------------------------------------------')
#  میدهیم precision مامیتوانیم برای اعداد دقت مشخص کنیم که به ان 
# درواقع داریم میگویم سن ما یک مقدار باشد یک عدد از اعشار داشته باشد و به سمت بالا رند میشود
sen=43.5433323
combind3 = 'Hello my Name is ayin Im {age:1.1f}'.format(age=sen)
print(combind3)
print('------------------------------------------------')

# نیز استفاده کنیم f  خب ما میتوانیم از فرمت 

fString_name="Hadi"
fString_family="mahdavi"
fString_age=32
fStringCombind = f"my name is {fString_name} - {fString_family} Im ({fString_age}) Years Old"

print(len(fStringCombind))