
#   یعنی من نمیخوام کاری اناجم بدم برو دستور بدیPath دستور  
# برای مثال اگر بخواهیم حلقه ای بزنیم و فعلا انتظار داریم کاری برای ما انجام ندهد

for a in [1,2,3,4]:
    pass 

# است کاره شکستن را حلقه را انجام میدهد break دستور بعدی دستور 

for i in [2,3,4,5,6]:
    if(i == 5) : break
    print(i)

# continue یعنی ادامه بده :
print('----------------------------')


for a in [5,4,3,2,1]:
    if(a == 3): continue
    print(a)

    print('----------------------------')

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for b in numbers:
    if(b % 2 != 1): continue
    print(b);


print('----------------------------')    

n = 0

while  n < 20:
    n += 1
    if n % 5 == 0 :
        print("hope")
        continue;
    if n == 17: break;
    print(n)


for key in range(10):
    if(key == 5): break
    print(key)    