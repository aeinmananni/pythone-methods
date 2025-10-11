print("While ....")

i: int = 0

while i < 5:
    print("Hello World : ")
    i += 1

print("-------------------")

count: int = 4
while count <= 10:
    print("Number is : ", count)
    count += 1


print("------------------")

password: str = ""

while password != "1234":
    password = input("رمز ورود خود را وارد کنید : ")


print("دسترسی مجاز : ✅")

print("---------------------------------")

total: int = 0

while True:
    num = int(input("Please set number if(Exist set zero) : "))

    if num == 0:
        break

    total += num

print("Total => ", total)
