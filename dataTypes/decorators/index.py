def add(a: int, b: int):
    return a + b


def Caculate(a: int, b: int, cb) -> int:
    return cb(a, b)


result: int = Caculate(3, 4, add)

print("Reault : ", result)
