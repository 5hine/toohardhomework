cost = 0
unit_price = 5
discount_price = 0
for i in range(20*2):
    if cost < 100:
        discount_price = unit_price
    elif 100 < cost < 150:
        discount_price = unit_price*0.8
    elif 150 < cost < 400:
        discount_price = unit_price*0.5
    else:
        discount_price = unit_price
    cost += discount_price

print("小明每个月交通费用是%d" % cost)
