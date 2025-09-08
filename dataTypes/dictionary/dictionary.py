# درواقع دیکشنری مانند ابجکت ها عمل میکند

score ={
    "raizi":43,
    "fizick":29,
    "zist":68
}

print(score["fizick"])
print('-------------------------')
print(score["raizi"])


print('-------------------------')

student_score=[score,{"GGG":54,"RRR":32,"QQQ":14},]
SCORE = student_score[0]
print("SCORE_STUDENTS : ",SCORE["raizi"])

# میتوانیم کلید هارا استخراج کنیم
print("KEYS :" , SCORE.keys())
# => output : KEYS : dict_keys(['raizi', 'fizick', 'zist'])


# میتوانیم مقدار هرکلید را نیز داشته باشیم
print("VALUES : " , SCORE.values());
# => output:VALUES :  dict_values([43, 29, 68])

# میبینیم که هر گروه را به صورت ایتم درست کنیم
print("ITEMS : ",SCORE.items())
# => output: ITEMS :  dict_items([('raizi', 43), ('fizick', 29), ('zist', 68)])

print('-------------------------')

person ={
     "id":1,
     "firstName":"Hossine",
     "lastName":"ahmadi",
     "age":32
}

print("DICTIONARY : (keys) ",person.keys())
# output => DICTIONARY : (keys)  dict_keys(['id', 'firstName', 'lastName', 'age'])

print("DICTIONARY : (values) ",person.values())
# => DICTIONARY : (values)  dict_values([1, 'Hossine', 'ahmadi', 32])


print("DICTIONARY : (items) ",person.items())
# output => DICTIONARY : (items)  dict_items([('id', 1), ('firstName', 'Hossine'), ('lastName', 'ahmadi'), ('age', 32)])


print('-------------------------')

# میتوانیم با کمک این متد مقدار یک کلید را دریافت کنیم
# نکته جالبی که وجود دارد اگر پراپرتی با این مقدار وجود نداشته باشد
# خطلایی نشان نمیدهد فقط چیزی برنمیگرداند

Colors={
    "red":"#red",
    "blue":"#blue",
    "yellow":"#yellow"
}

print("DICTIONARY : (get) " , Colors.get("red"))
# => output : DICTIONARY : (get())  #red

# میتوانیم به این صورت شریطی بنویسیم اگر کلیدی با این نام وجود نداشت -1 برای ما برگردان

print("DICTIONARY : (Conditional : get) " , Colors.get("ss",-1))
# => output : DICTIONARY : (Conditional : get)  -1


print('-------------------------')

Numbers ={
     "list1":[1,2,3,4,5],
     "list2":[6,7,8,9,10]
}

print("Get me Index :",Numbers["list1"][3])
# output => Get me Index : 4

print('-------------------------')
# میتوانیم به این صورت نیز پیاده سازی را انجام دهیم

class_names = {"1":["ahmad","Reza","gavad"],"2":["sara","nahid","rodabeh"]}

print("class_names : " , class_names["1"][2])
# output => class_names :  gavad

print("SLICE : ",class_names["2"][0][-1].upper())
# output => SLICE :  A

class_names["3"] = ["hotan","mohammad","yones"]

print(class_names)
# output => {'1': ['ahmad', 'Reza', 'gavad'], '2': ['sara', 'nahid', 'rodabeh'], '3': ['hotan', 'mohammad', 'yones']}