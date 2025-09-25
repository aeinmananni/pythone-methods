def is_even(n:int):
    return n % 2 == 0




myNumber = is_even(13)
print("is Even ? " ,myNumber)

print("-----------------------")


def number_of_even(nums:list[int]):
    counter:int = 0
    for i in nums:
        if(is_even(i)):
            counter += 1
    return counter


NUMBERS_LIST:list[int] =[1,2,3,4,12,65,77,22] 
EVEN_CHAECKS = number_of_even(NUMBERS_LIST);
print("The Evens Numbers : " ,EVEN_CHAECKS)

print("--------------------")


def any_even_in_list(nums:list[int]):
    for i in nums:
        if(is_even(i)):
            return True
    return False 
        
ANY_EVEN_IN_LIST = any_even_in_list([1,35,5,7,2])
print("Have Even ? " , ANY_EVEN_IN_LIST)


print("----------------------------")

def largest(nums:list[int]):
    largest_number:int = nums[0]
    for n in nums:
        if largest_number < n:
            largest_number = n
    return largest_number

NUMBERS_LIST_MODEL = [0,1,2,3,54,4,5,6,7,8]
LARGEST_NUMBER = largest(NUMBERS_LIST_MODEL)

print("Get largest list : " , LARGEST_NUMBER);


print("--------------")

def my_odds(nums:list[int]):
    odd_list:list[int] =[]
    for n in nums:
        if not is_even(n):
            odd_list.append(n)
    return odd_list

print("Odd Numbers List : " , my_odds([22,54,1,13,66]))


