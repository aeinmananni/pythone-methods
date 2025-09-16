print("Conditions")

print("--------------------------")

if(True):
    print("Hello World")

age=23
if(age > 20):
    print("Yes isValid")
else:
    print("is Not Valide !")    

print("-------------rols example!-------------")

rols="GEST"
MESSAGE_ROLS="Result login : wellcom "


if rols == "ADMIN": print(f" {MESSAGE_ROLS} {rols}")
elif rols =="GEST":print(f" {MESSAGE_ROLS} {rols}")
else:print("your Not Login!")

print("-------------football example!-------------")

action="PASS"
MESSAGE_FOOTBALL= "Take a "
if action == "SHOOT":
    print(f"{MESSAGE_FOOTBALL} {action}")
elif action == "PASS":
    print(f"{MESSAGE_FOOTBALL} {action}")
elif action == "GOOL":
    print(f"{MESSAGE_FOOTBALL} {action}")
else :
    print("What are you doing now!")            