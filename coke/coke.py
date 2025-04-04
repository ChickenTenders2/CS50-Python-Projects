original_price = 50
price = 50
acceptable_coins = [5, 10, 25]
total_payment = 0

while True:
    print(f"Amount Due: {price}")
    payment = input("Insert Coin: ")
    if payment.isnumeric() == True:
        payment = int(payment)
        total_payment += payment
        if payment < 0 or payment not in acceptable_coins:
            continue
        else:
            if payment < price:
                price = price - payment
                continue
            else:
                change = total_payment - original_price
                print(f"Change Owed: {change}")
                break
