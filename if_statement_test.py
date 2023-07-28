house_price = 1000000 #price of the house
is_good_credit = False

if is_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Your down payment is ${down_payment}")
