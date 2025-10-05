# pypi تمام لیست کتابخانه های پایتون توی این سایت میتونیم پیداش کنیم 
import emoji
from tqdm import tqdm
import time
import myMode
from program_module import Programer_function_module
from package import visited_normal_range 
red_heart  = emoji.emojize("Ayin :red_heart:")

hand = emoji.emojize(":thumbs_up:")
print("Result : " , red_heart)
print("Result : " , hand)


# for i in tqdm(range(1000)):
#     time.sleep(0.1)


print("Function : " ,myMode.my_func_print(),myMode.pi)    
print("Programmer : " , Programer_function_module())
print("Visted Normal Range : " , visited_normal_range.visited_normal_range())

print(f"What your name {__name__}")