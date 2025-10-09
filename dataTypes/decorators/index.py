def add(a: int, b: int):
    return a + b


def Caculate(a: int, b: int, cb) -> int:
    return cb(a, b)


result: int = Caculate(3, 4, add)

print("Reault : ", result)

print("-----------------run_on_even----------------")


def run_on_even(fn) -> str:
    import datetime
    now = datetime.datetime.now()
    minute = now.minute
    if minute % 2 == 0:
        return fn()
    else :
         return "Hissssss!"





def say_Hello1() -> str:
    return "Hello ! im Ayin Mannani"

def say_bye1():
    return "Say Bye ! Ayin Mannani"

SAY_HELLO:str = run_on_even(say_Hello1)
SAY_BYE:str = run_on_even(say_bye1)

print(SAY_HELLO)
print(SAY_BYE)

print("---------------run_on_odd----------------")

def run_on_odd(fn):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 1:
            return fn()
        else:
            return "Not Exist !"
    return wrapper  


@run_on_odd
def say_hello2():
    return "Say Hello ! Ayin Mannani"
@run_on_odd
def say_bye2():
    return "Say bye! Ayin Mannani"

SAY_HELLO2 = say_hello2()
SEY_BYE2 = say_bye2()

print(SAY_HELLO2)
print(SEY_BYE2)