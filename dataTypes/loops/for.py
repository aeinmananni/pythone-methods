
numbers=[1,2,3,4,5,6]

for this_item in numbers:
    print("Items : " ,this_item)

# ----------------------------------------

messages="This is my Message"
for messge in messages:
    print(messge)

# ----------------------------------------

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number} is Odd")    
        

count=0

for counter in numbers:
    if counter % 2 == 0:
        count  += 1

print("Loops Counter" ,count)
# ----------------------------------------        



