
fruits :list[str] = ["Apple","bananna","cherry"]

for fruit in fruits:
    print("1- fruits " , fruit)

print("--------------------------------")
firstName = "My name is ayin"

for name in firstName:
    print(name)

print("--------------------------")

for number in range(5):
    print(number)

print("--------------------------")

for number in range(2,6):
    print(number)

print("--------------------------")
for number in range(0,len(firstName),2):
    print(number)
print("---------------------------")

students = [{"firstName":"farhad","lastName":"rasoli","age":32},{"firstName":"sara","lastName":"abasi","age":24}]

for stds in students:
    for key in stds:
        print(key, ":",stds[key])

print("-----------------")

person = {"name":"alireza","age":28}

for p in person:
    print(p, person[p])


hobbise = ["Sports","Movies","Created Project"]

for index,hobbi in enumerate(hobbise):
    print(index , ":" , hobbi)


print("------------------------")

even = []
for r in range(20):
    if(r % 2 == 0):
        even.append(r)

print(even)
        