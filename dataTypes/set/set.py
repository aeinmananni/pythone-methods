# توی مجموعه ها از هرچیزی فقط یکبار میتوانیم داشته باشم
# یعنی نمیتوانیم اعضا تکراری در ان ذخیره کنیم
# در حالتی که داریم ادد میکنیم نمیتوانیم چند عدد را ادد کنیم فقط میتوانیم 1 عدد اضافه کنیم

mySets = set()

mySets.add(3);
mySets.add(4);
mySets.add(5);

print(mySets)

print("--------------------");

personList = set();
personList.add("Ayin");
personList.add("Hadiss");
personList.add("drazi");

print("Person List : " , personList);

print("--------------------");

# میتوانیم مجموعه هارو بصورت اتحاد دربیاوریم : (Union)

numbers1 = set();
numbers2 = set();

numbers1.add(1);
numbers1.add(2);
numbers1.add(3);
# --------------------
numbers2.add(4);
numbers2.add(5);
numbers2.add(6);
union_combinde = numbers1.union(numbers2)


print("Union : ", union_combinde)

print("--------------------");

# خب حالا میتوانیم اشتراک های یک مجموعه را نیز بدست اوریم

names1=set();
names1.add("ahmad");
names1.add("sara");
names1.add("rasol");
# ---------------------
names2= set();
names2.add("hossine");
names2.add("sara");
names2.add("amirReza");

intersection_names = names1.intersection(names2)

print("Give me Intersection List : " , intersection_names);

print("--------------------");

# خب نوع دیگری که میتوانیم مجموعه هارا تعریف کنیم

animals = set(["woff","cat","elephent","jiroft","monky"])

animals.add("dog")
animals.add("brith")

print(animals)
print("--------------------");
# میتوانیم اجتماع و یا اشتراک را به روش های زیر نیز حل کنیم

firstNames1 = set(["hootan","jalal","mehdi","rocksana","sara"]);
firstNames2 = set(["omid","rasol","sara","mehdi","norAli","fatheme"])
# union
u = firstNames1 | firstNames2 

# intersection 
i = firstNames1 & firstNames2 
print("Intersection : ", i)

# خب حالا میخواهیم برسی کنیم اعضایی که درون مجکعه اول هستند اما درون مجموعه دوم نیستند  یا تفاضل
d = firstNames1.difference(firstNames2);
dMinus = firstNames1 - firstNames2

print("difference1 : " , d)
print("difference2 : " , dMinus)

# 🔸 اگر بخوای تفاضل متقارن (symmetric difference) بگیری (یعنی همه‌ی عناصری که فقط در یکی از مجموعه‌ها هستند و در هر دو مشترک نیستند):
sym_diff = firstNames1 ^ firstNames2
print(sym_diff)  # {1, 2, 5, 6}
