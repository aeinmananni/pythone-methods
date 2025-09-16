# boolean
# عبارت هایی که میتواند درست یا غلط باشد
# None : یعنی هنوز بهش مقدار ندادم
age = 45;
print(age >30)
print(age == 45)
print(age <= 44)

# output =>True

# ----------------------
print(type(None))
# output => NoneType

# or

condition1=3;
condition2=1000
print('OR : ' ,condition1 >= 4 or condition2 < 1000) 
# output False

print('OR : ' ,condition1 >= 3 or condition2 < 1000)
# output True

score=13.2
age = 22
print("AND : ",score >= 10 and age < 20)
print("AND : ",score >= 10 and age >= 20)

# not

language=True
print("NOT ",not(language))

# functions

numbers='123';
print("Is Digit :" ,numbers.isdigit());

# in
listNumber1 = [1,2,3,4,"ayin"]
print("Check in:" , 1 in  listNumber1)

animals = {"dogs":3,"horse":3,"ships":15}
print("Check in:" , "horse" in  animals)