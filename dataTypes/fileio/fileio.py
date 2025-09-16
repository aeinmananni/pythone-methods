# مامیتوانیم متغییری داشته باشم که از یک فایل میخواند و میتوانیم محتوای ان فایل را درجاییذخیره کرده ویا
# درفایل دیگری ان را بنویسیم
# fileName = open("myFile.txt") : 
# درواقع ما توانایی امکان خواندن و نوشتن یک فایل را به متغغیر خوئد داده ایم
# درواقع ما متغغیری داریم که به اوپن شده فایل ما اشاره میکد
# ------------------------------------------------

fileName = open("myFile.txt");
print(type(fileName))

print("--------------------------");

# read() تمام فایل را میخواند
message = fileName.read(); 
print("read() Method : \n" ,message)

# زمانی که فایلی را درون متغییری میریزیم سر فایل می ایستد تاببنید ما میخواهیم چه کاری انجام دهیم
# fileName.read() و ما با این دستور محتوای فایل را میخوانیم
# و درواقع بعد از خواندن به ته فایل رسیده است
# seek : یعنی حرکت کردن و اشاره به این میکند الان درکجا قرار دارد
# درنهایت میبینیم در کنسول زیر دیگر خروجی نداریم
print("--------------------------");
print("repeat file read 1 : " , fileName.read())

# --------------------------------------------
# حالا برای اینکه مجدد به اشاره گر به ابتدای فایل اشاره کند میتوانیم این کار را انجام دهیم
# این دستور یعنی اشاره گر به ابتدا برگردد
print("--------------------------");
fileName.seek(0) 
print("repeat file read 1 : \n" , fileName.read())
fileName.close();
print("--------------------------");


# اما بهترین روش استفاده از دستور with هست. اینطوری لازم نیست دستی فایل رو ببندی:

with open("myFile.txt","r") as file:
     Message_box = file.read();
     file.seek(0)
print("Message Box Read : " ,Message_box)
#  بعد از خروج از بلاک بسته میشود

print("--------------------------")

# ✅ نکته ۲: حالت‌های باز کردن فایل

# "r" → فقط خواندن (پیش‌فرض)

# "w" → فقط نوشتن (محتوای قبلی پاک میشه)

# "a" → اضافه کردن به انتهای فایل

# "r+" → خواندن و نوشتن همزمان


#  w+ اگر فایلی در دایرکتوری وجود نداشت میتوانیم به این صورت ان را اضافه کنبیم 
with open("myFile.txt" , "+w") as file:
     file.write("\n my file have new Message\n im so happy\n im creatore Best Coding life");
     file.seek(0)
     addMessage = file.read();
print("Add New Message is File : " , addMessage)

print("--------------------------")

with open("newFile.txt","+w") as file:
     file.write("my name is ayin mannani");
     file.seek(0)
     fullName = file.read();
print("My fullName is Read File : " , fullName)
print("--------------------------")

with open("newFile.txt","a+") as file:
     file.write("\n this is my name message in file");
     file.seek(0)
     fileReader = file.read();
print("file Reader output : " ,fileReader)

print("--------------------------")

with open("myFile.txt","r") as file:
     for line in file:
        #    strip : فاصله های اضافی رو حذف میکنه
          print("Read line" ,line.strip());
print("--------------------------")

# درنهایت به شکل ارایه ای از خط ها برای ما برمیگرداند که در دیتاهای بزرگ به صرفه نخواهد بود
# readlines: تمام خطوط را در قالب یک لیست می‌دهد
with open("file-reader.txt", "r") as file:
    all_lines = file.readlines()
    print("Readlines:", all_lines)
    file.seek(0)

print("--------------------------")

# readline: فقط یک خط را برمی‌گرداند
with open("file-reader.txt", "r") as file:
    first_line = file.readline()
    while first_line.strip() == "":
          first_line = file.readline()
    print("Readline:", first_line.strip())
