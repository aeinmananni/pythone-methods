
import random
computer_number:int = random.randint(1,20)




def welcom():
    print("Welcom to funny Games  !")
    print("I will gess a number between 1 100 and")
    print("you have to gess it...")
    print("go go go go =>")


def finish(number:int,count:int) -> int:
    print("Good Gamse : ")
    print(f"my number is was {number} and youe found it in {count} gesses")
    answer = input("Do you want to playing again ? (Y/N)")
    if answer.upper() in ["Y" , "YES" , "ARE"] :
        return True
    else :
        return False

def win(computer_number:int,gess:int):
    return computer_number == gess


def get_a_gess():
    ansswer = input("What is your gest ?")
    return int(ansswer)


def answer(computer_number:int,gess:int):
    if computer_number > gess:
        return "My number is larger"
    elif computer_number < gess:
        return "My number is smaller"
    else :
        return "Ooh very good yout win!"


welcom()
continue_playing : int = True

while(continue_playing):
    gess:int = 0
    count:int = 0
    while not win(computer_number,gess):
        gess = get_a_gess()
        count += 1
        print(answer(computer_number,gess))

    continue_playing = finish(computer_number,count)