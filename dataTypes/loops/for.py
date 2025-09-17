
numbers=[1,2,3,4,5,6]

for this_item in numbers:
    print("Items : " ,this_item)
# output  =>  
            # Items :  1
            # Items :  2
            # Items :  3
            # Items :  4
            # Items :  5
            # Items :  6
# ----------------------------------------

messages="This is my Message"
for messge in messages:
    print(messge)
# output =>    
            # T
            # h
            # i
            # s

            # i
            # s

            # m
            # y

            # M
            # e
            # s
            # s
            # a
            # g
            # e
print("# ----------------------------------------")

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number} is Odd")    
        
# output => 
            # 1 is Odd
            # 2
            # 3 is Odd
            # 4
            # 5 is Odd
            # 6     
print("# ----------------------------------------")     


count=0
for counter in numbers:
    if counter % 2 == 0:
        count  += 1

print("Loops Counter" ,count)
# output => Loops Counter 3

print("# ----------------------------------------")        

my_tuple = (12,3,4,5,6,"ayin")

for _t in my_tuple:
    print(_t)
# ouput => 
            # 12
            # 3
            # 4
            # 5
            # 6
            # ayin          
print("# ----------------------------------------") 

tuple2 = ([1,2,3,4,5,6],[7,8,9,10],[11,12,13,14,15,16])

for t in tuple2:
    for arr in t:
        print(arr)
# output =>
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # 11
        # 12
        # 13
        # 14
        # 15
        # 16

print("# ----------------------------------------")      

#   را انجام دهیمunPack در این مرحله میخواهیم 
personal=(("hadi",32),("ayin",28),("Reza",77))

for p in personal:
    firstName , age = p
    print(f"my name is {firstName} im ({age}) Years Old")

# output => 
            # my name is hadi im (32) Years Old
            # my name is ayin im (28) Years Old
            # my name is Reza im (77) Years Old


print("# ----------------------------------------")   
# UnPack روش دیگری برای 

for firstName ,age in personal:
    print(f"UnPacked {firstName} and {age}")

# output =>
            # UnPacked hadi and 32
            # UnPacked ayin and 28
            # UnPacked Reza and 77


print("# ----------------------------------------")     

# 

BMI = {
     "Hadi":(13,176),
     "sara":(34,187),
     "morteza":(23,190),
     "ehsan":(55,182),
}

# دراین حالت فقط کلید هارا

for bmi in BMI:
    print(bmi)

# output =>
            # Hadi
            # sara
            # morteza
            # ehsan


print("# ----------------------------------------")    

for bmi in BMI:
    print(f"{bmi} : {BMI[bmi]}")

# output =>
            # Hadi : (13, 176)
            # sara : (34, 187)
            # morteza : (23, 190)
            # ehsan : (55, 182)


print("# ----------------------------------------")    

for bmi in BMI:
    print(f" {BMI[bmi][0]}")

# output =>
            # 13
            # 34
            # 23
            # 55

print("# ----------------------------------------")    

for bmi in BMI:
    age,scor = BMI[bmi]
    print(f"AGE : {age} SCORE: {scor}")    

# output =>
            # AGE : 13 SCORE: 176
            # AGE : 34 SCORE: 187
            # AGE : 23 SCORE: 190
            # AGE : 55 SCORE: 182


print("# ----------------------------------------") 

# خب حالا اگربخواهیم بجای فقط کلید تمام ایتم های داخل دیکشنری را در کنار هم برگردانیم

for item in BMI.items():
    print("ITEMS : " , item)

# output =>
            #ITEMS :  ('Hadi', (13, 176))
            # ITEMS :  ('sara', (34, 187))
            # ITEMS :  ('morteza', (23, 190))
            # ITEMS :  ('ehsan', (55, 182))
print("# ----------------------------------------") 

#  میتوانیم ایتم ها و یا دیتا های ان هارا از هم جدا کنیم
# به طورپیش فرض روی همچین حالتی برسی میشوند که فقط در مرحله اول میتواند کلید هارا برگرداند BMI.keys()


for item,data in BMI.items():
    print(f"Items : {item} ---- Data : {data}")

# output =>
            # Items : Hadi ---- Data : (13, 176)
            # Items : sara ---- Data : (34, 187)
            # Items : morteza ---- Data : (23, 190)
            # Items : ehsan ---- Data : (55, 182)            

print("# ----------------------------------------") 
# خب میتوانیم بر اساس ولیو ها فقط دیتا هارا برگردانیم

for values in BMI.values():
    print(f"Values : {values}")

# output =>
            # Values : (13, 176)
            # Values : (34, 187)
            # Values : (23, 190)
            # Values : (55, 182)    