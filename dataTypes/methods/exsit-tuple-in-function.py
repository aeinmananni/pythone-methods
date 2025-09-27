def  get_odd(nums:list[int]):
    odd:list[int] = []
    counter:int = 0
    for n in nums:
        if not n % 2 == 0:
            counter += 1
            odd.append(n)
    return counter,odd       

lists:list[int] = [1,2,3,4,5,6,7,8,9]
counter , oddslist = get_odd(lists)
# میتوانیم در نمایش جداکننده هارا نیز به پرینت خود اضافه کنیم
print("My Odd : " , counter ,oddslist,sep="|")

# output => My Odd :  5 [1, 3, 5, 7, 9]

print("----------------------")

def jam_zarb(n1:int,n2:int):
    jam:int = n1 + n2
    zarb:int = n1 * n2
    return jam , zarb

print("JAM_ZARB : " , jam_zarb(15,12))
# output => JAM_ZARB :  (27, 180)

print("-----------donations----------")

donations:dict[str,int] = {
     "javad" : 300,
      "sara" :500,
      "rasol" : 12,
      "hojat":1300
}

def donation_analysis(don:dict[str,int]):
    person:str = ""
    total:int = 0
    count:int = 0
    max_donation:int = -1
    for name,value in don.items():
        total += value
        count += 1
        if value > max_donation:
            person = name
            max_donation = value
    avrage = total / count    
    return avrage , total , person



result_donations = donation_analysis(donations)        
print("Result donations : " , result_donations)

# output = > Result donations :  (528.0, 2112, 'hojat')