import time

def timing_decorator(function):
    def wrraper(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        print(f"{end - start:.6f}") 
        return result
    return wrraper

@timing_decorator
def create_list(n):
    return [i for i in range(1,n + 1)]


n = int(input("را وارد کن n عدد :"))
result = create_list(n)
print("لیست:", result)