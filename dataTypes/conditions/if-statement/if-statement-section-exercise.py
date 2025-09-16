
PRICE=55000

if PRICE > 50000:
    final_price = PRICE * (1 - 20 / 100)
elif 20000 <= PRICE <= 50000:
    final_price= PRICE * (1 - 10 / 100)
else:
    final_price= PRICE


print(int(final_price))