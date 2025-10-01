def zarb(a:int,b:int):
    return a * b

result = zarb(3,4)
print("result : ", result)

print("--------------------")

def args_function(*input:tuple) -> int:
    counter:int = 1
    for a in input:
        counter *= a
    return counter    

COUNTER_RESULT:int = args_function(2,3,4)

print("COUNTER : ",COUNTER_RESULT)

print("--------------------")

def Personal(**input:dict) -> dict:
    print(input)

Personal(firstName="ayin",lastName = "Mananni")    

print("-----------------------")

def Caculate(**input:dict) -> int:
    if "tool" in input:
        return input['tool'] * input["ertefa"]
    if "shoa" in input:
        return input["shoa"] * 3.14 * input["ertefa"]
    return -1

CALCULATE_RESULT:int = Caculate(shoa=12,ertefa=14)

print("Calculate Result : " , CALCULATE_RESULT)