amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    user_coin = int(input("Insert Coin: "))
    if user_coin == 25 or user_coin == 10 or user_coin == 5:
        amount_due = amount_due - user_coin
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            break
    else:
        print("Wrong coin!")


