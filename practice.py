import csv
balance = 5000
user_pin = 12345

def money_transfer():
    global balance
    global user_pin
    amount = int(input("Enter Amount: "))
    reference = int(input("Enter Reference: "))
    pin = int(input("Enter Menu Pin: "))
    if pin == user_pin:
        if balance >= amount:
            balance -= amount
            print("Congratulations your payment is successfully")
    else:
        print('Your pin is false')
money_transfer()