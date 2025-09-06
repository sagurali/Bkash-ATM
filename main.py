import os
import time
import sys

user_pin = 12345


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_user_data():
    try:
        with open('userdata.txt', 'r') as f:
            return dict(line.strip().split(',') for line in f)
    except FileNotFoundError:
        return {}


def save_user_data(users):
    with open("userdata.txt", "w") as f:
        for mobile, pin in users.items():
            f.write(f"{mobile},{pin}\n")


def reset_pin():
    users = load_user_data()
    mobile_number = input("Enter your mobile number: ")
    if mobile_number not in users:
        print("Mobile number not found.")
        return
    new_pin = input("Enter your new PIN: ")
    confirm_pin = input("Confirm your new PIN: ")
    if new_pin != confirm_pin:
        print("PINs do not match. Please try again.")
        return
    users[mobile_number] = new_pin
    if new_pin != confirm_pin:
        print("PINs do not match. Please try again.")
        return
    users[mobile_number] = new_pin
    save_user_data(users)
    print("PIN reset successful!")


def download_animation():
    animation_chars = ['|', '/', '-', '\\']

    for i in range(10):
        for char in animation_chars:
            sys.stdout.write(f'\rDownloading... {char}')
            sys.stdout.flush()
            time.sleep(0.1)

    print("\nDownload complete!")


def check_balance():
    try:
        with open("Bkash_Balence.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 100000


def update_balance(balance):
    with open("Bkash_Balence.txt", "w") as f:
        f.write(str(balance))


balance = check_balance()

clear_console()


def display_menu():
    print("\t\t Welcome to Personal Bkash \n")
    print(
        "========================================================================="
    )
    print("\t\t 1. Send money")
    print("\t\t 2. Send money to non-bkash user")
    print("\t\t 3. Mobile recharge")
    print("\t\t 4. Payment")
    print("\t\t 5. Cash out")
    print("\t\t 6. Pay Bill")
    print("\t\t 7. Download Bkash App")
    print("\t\t 8. My Bkash")
    print("\t\t 9. Reset PIN")
    print(
        "========================================================================="
    )


def money_transfer(number):
    global balance
    amount = int(input("Enter Amount: "))
    reference = int(input("Enter Reference: "))
    pin = int(input("Enter Menu Pin: "))

    if pin == user_pin:
        clear_console()
        if amount <= balance:
            balance -= amount
            update_balance(balance)
            print("Congratulations your payment is successfully😀\nNumber:",
                  number, "\nAmount:", amount, "\nCurrent Amount:", balance)
        else:
            clear_console()
            print('\t=============================================')
            print('\t\t\tInsufficient balance 😔')
            print('\t=============================================')
    else:
        clear_console()
        print('\t=============================================')
        print('\t\t\tWrong pin 😔')
        print('\t=============================================')


def non_bkash():
    global balance
    clear_console()
    number = int(input("Enter Receiver Number: "))
    Amount = int(input("Amount: "))
    Reference = int(input("Reference: "))
    pin = int(input("Enter Menu Pin: "))
    if pin == user_pin:
        clear_console()
        if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print(
                "Congratulations😀\nSend Money to non-bkash user is Successful \nNumber:",
                number, "\nAmount:", Amount, "\nCurrent Amount:", balance)
    else:
        clear_console()
        print('\t=============================================')
        print('\t\t\tWrong pin😔')
        print('\t=============================================')


def Mobile_Recharge(number):
    global balance
    Amount = int(input("Enter Amount: "))
    pin = int(input("Enter Menu PIN to confirm: "))

    if pin == user_pin:
        clear_console()
        if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print("Congratulations😀\nMobile Recharge SuccessFully \nNumber:", number,
                  "\nAmount:", Amount, "\nCurrent Amount:", balance)

    else:
        clear_console()
        print('\t=============================================')
        print('\t\t\tWrong pin😔')
        print('\t=============================================')


def send_Money():
    global balance
    Amount = int(input("Enter Amount: "))
    pin = int(input("Enter Menu PIN to confirm: "))
    if pin == user_pin:
        clear_console()
        if Amount <= balance:
            balance -= Amount
            update_balance(balance)
            print("Congratulations\nYour Cash Out is successful😀\nTo:", number,
                  "\nAmount:", Amount, "\nCurrent Amount:", balance)
    else:
        clear_console()
        print('\t=============================================')
        print('\t\t\tWrong pin😔')
        print('\t=============================================')


print("1. ATM")
print("2. BKASH")
method = int(input("Select Your Method: "))

if method == 1:
    clear_console()

    def load_balance():
        try:
            with open('atm_balance.txt', 'r') as file:
                return int(file.read())

        except FileNotFoundError:
            return 10000  # Default balance if the file doesn't exist

    def save_balance(balance):
        try:
            with open('atm_balance.txt', 'w') as file:
                file.write(str(balance))

        except Exception as e:
            print(f"Error saving balance: {e}")

    print('''
    --------------------     
    Enter your CARD...
    --------------------''')

    time.sleep(2)  # Delay to read card
    clear_console()

    password = 1234
    pin = int(input('''
    -------------------------
    Enter your ATM PIN: '''))
    clear_console()

    balance = load_balance()

    if pin == password:

        while True:
            print('''
                
     ______________________________  
    |                              |
    |  Main menu:                  |
    |       1 - View my balance    |
    |       2 - Withdraw cash      |
    |       3 - Deposit funds      |
    |       4 - Exit               |
    |______________________________|
                  ''')

            try:
                option = int(input('''
    -----------------
    Enter a choice: '''))
                clear_console()

                if option == 1:
                    print(" ------------------------------------")
                    print(f"| Your current balance is {balance}✅    |")
                    print(" ------------------------------------")

                elif option == 2:
                    withdraw_amount = int(
                        input('''
    ---------------------------------------
    Please enter withdrawl amount: '''))
                    clear_console()

                    if withdraw_amount <= balance:
                        balance -= withdraw_amount
                        save_balance(balance)

                        print("----------------------------------------")
                        print(
                            f"- BD {withdraw_amount} is debited from your account✅")
                        print(f"- Your current balance is {balance} BD")
                        print("----------------------------------------")

                    else:
                        print("Insufficient funds...⚠️")

                elif option == 3:
                    deposit_amount = int(
                        input('''
    ---------------------------------------                                         
    Please enter deposit amount: '''))
                    clear_console()

                    if deposit_amount > 0:
                        balance += deposit_amount
                        save_balance(balance)

                        print("----------------------------------------")
                        print(
                            f"- BD {deposit_amount} is credited to your account✅")
                        print(f"- Your current balance is {balance} BD")
                        print("----------------------------------------")

                    else:
                        print('''
    ----------------------------                        
    Invalid deposit amount...
    ----------------------------''')

                elif option == 4:
                    print('''
    ----------------------------------------                    
    Thank you for using the 🏧. Goodbye!👋
    ----------------------------------------''')
                    break

                else:
                    print('''
    --------------------------------------                    
    Invalid option. Please try again...🔄
    --------------------------------------''')
                    break

            except ValueError:
                print('''
    ---------------------------------------                
    Invalid... Please enter a valid number
    ---------------------------------------''')

    else:
        print('''
    ---------------        
    Wrong pin!!!❎
    ---------------''')


elif method == 2:
    clear_console()
    display_menu()
    user_input = int(input("Enter Your Choice: "))

    if user_input == 1:
        clear_console()
        number = int(input("Enter Receiver Account Number: "))
        money_transfer(number)
    elif user_input == 2:
        non_bkash()

    elif user_input == 3:

        clear_console()
        print("1. Banglalink")
        print("2. GrameenPhone")
        print("3. Teletalk")
        print("4. Robi")
        user_sim = int(input("Select Your Sim: "))

        if user_sim == 1:
            clear_console()
            number = int(input("Enter Banglalink Number: "))
            Mobile_Recharge(number)

        elif user_sim == 2:

            clear_console()
            number = int(input("Enter GrameenPhone Number: "))
            Mobile_Recharge(number)

        elif user_sim == 3:
            clear_console()
            number = int(input("Enter Teletalk Number: "))
            Mobile_Recharge(number)

        elif user_sim == 4:
            clear_console()
            number = int(input("Enter Robi Number: "))
            Mobile_Recharge(number)

    elif user_input == 4:
        clear_console()
        number = int(input("Enter Your Merchant Account: "))
        money_transfer()

    elif user_input == 5:
        clear_console()
        print(
            "Only Agent Number can transfer money.\nIf you are agreed please enter 1 or either enter 2"
        )
        user_decision = int(input(""))
        if user_decision == 1:
            clear_console()
            number = int(input("Enter Receiver Number: "))
            send_Money()
        elif user_decision == 2:
            clear_console()
    elif user_input == 6:
        clear_console()
        print("\t\t 1.Electricity")
        print("\t\t 2.Gas")
        print("\t\t 3.Water")
        print("\t\t 4.Internet and Phone")

        payBillInput = int(input("Select Bill: "))
        if payBillInput == 1:
            clear_console()
            print("\t\t 1.Palli Bidyut")
            print("\t\t 2.DESCO")
            billType = int(input("Select Bill Type: "))
            if billType == 1:
                clear_console()
                print("\t\t Palli Bidyut")
                print("\t\t 1.Bill Breakdown")
                print("\t\t 2.Make Payment")

                paymentBill = int(input("Select One: "))
                if paymentBill == 1:
                    clear_console()
                    print("\t\t Bill Breakdown")
                    print("\t\t 1.Input Meter Number")
                    print("\t\t 2.Saved Account")

                    paymentMethod = int(input("Select One: "))
                    if paymentMethod == 1:
                        clear_console()
                        meterNumber = int(input('Meter Number:'))
                        Amount = int(input('Enter Amount:'))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print(
                                    "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif paymentMethod == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentBill == 2:
                    clear_console()
                    print("\t\t Make Payment")
                    print("\t\t 1.Input Meter Number")
                    print("\t\t 2.Saved Account")

                    paymentMethod = int(input("Select One: "))
                    if paymentMethod == 1:
                        clear_console()
                        meterNumber = int(input('Meter Number:'))
                        Contact = int(input('Contact Number:'))
                        Amount = int(input('Enter Amount:'))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print(
                                    "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif paymentMethod == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif billType == 2:
                clear_console()
                print("\t\t DESCO")
                print("\t\t 1.Bill Breakdown")
                print("\t\t 2.Make Payment")
                paymentBill = int(input("Select One: "))
                if paymentBill == 1:
                    clear_console()
                    print("\t\t Bill Breakdown")
                    print("\t\t 1.Input A/C Number")
                    print("\t\t 2.Saved Account")

                    paymentMethod = int(input("Select One: "))
                    if paymentMethod == 1:
                        clear_console()
                        accountNumber = int(input('Enter Account Number:'))
                        Amount = int(input('Enter Amount:'))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print(
                                    "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif paymentMethod == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif billType == 2:
                    clear_console()
                    print("\t\t Make Payment")
                    print("\t\t 1.Input Account Number")
                    print("\t\t 2.Saved Account")

                    paymentMethod = int(input("Select One: "))
                    if paymentMethod == 1:
                        clear_console()
                        meterNumber = int(input('Enter Account Number:'))
                        Contact = int(input('Contact Number:'))
                        Amount = int(input('Enter Amount:'))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print(
                                    "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif paymentMethod == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
        elif payBillInput == 2:
            clear_console()
            print("\t\t Gas")
            print("\t\t 1.Jalalabad Gas")
            print("\t\t 2.Sundarban Gas")
            print("\t\t 3.Paschimanchan Gas")
            print("\t\t 4.Karnaphuli Gas")

            gas_name = int(input("Select Your Gas: "))
            if gas_name == 1:
                clear_console()
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Customer Code Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Input Grahok Shonket No. "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif gas_name == 2:
                clear_console()
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Customer Code Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Input Grahok Shonket No. "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif gas_name == 3:
                clear_console()
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Customer Code Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Input Grahok Shonket No. "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif gas_name == 4:
                clear_console()
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Customer Code & Mobile No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter Customer Code & Mobile No. "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Grahok Shonket No.")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Input Grahok Shonket No. "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Gas Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
        elif payBillInput == 3:
            clear_console()
            print("\t\t Water")
            print("\t\t 1.Dhaka WASA")
            print("\t\t 2.Chattogram WASA")
            print("\t\t 3.Rajshahi WASA")
            print("\t\t 4.Khulna WASA (Metered)")

            waterBill = int(input("Enter Your Bill"))
            if waterBill == 1:
                clear_console()
                print("\t\t Dhaka WASA")
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Bill Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter Bill Number"))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif waterBill == 2:
                clear_console()
                print("\t\t Chattogram WASA")
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Bill Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter Bill Number"))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif waterBill == 3:
                clear_console()
                print("\t\t Rajshahi WASA")
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Bill Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter Bill Number"))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
            elif waterBill == 4:
                clear_console()
                print("\t\t Khulna Wasa")
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Bill Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input Bill Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter Bill Number"))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Water Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
        elif payBillInput == 4:
            clear_console()
            print("\t\t 1.BTCL")
            internetBill = int(input("Choose one: "))
            if internetBill == 1:
                clear_console()
                print("\t\t 1.Check Bill")
                print("\t\t 2.Make Payment")

                paymentMethod = int(input("Select Your Method: "))
                if paymentMethod == 1:
                    clear_console()
                    print("Check Bill")
                    print("\t\t 1.Input RYYMM Area code + Phone Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter RYYMM Area code + Phone Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Internet Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
                elif paymentMethod == 2:
                    clear_console()
                    print("Make Payment")
                    print("\t\t 1.Input RYYMM Area code + Phone Number")
                    print("\t\t 2.Saved Accounts")
                    checkBillInput = int(input("Select One: "))
                    if checkBillInput == 1:
                        clear_console()
                        ghahokSonketNumber = int(
                            input("Enter RYYMM Area code + Phone Number: "))
                        MonthYear = int(input("Month and Year mmyyyy: "))
                        pin = int(input("Enter Menu PIN: "))
                        if pin == user_pin:
                            clear_console()
                            print("Congratulations Your Internet Bill is complete!")
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    elif checkBillInput == 2:
                        clear_console()
                        print("Sorry, There is no beneficiary")
    elif user_input == 7:
        clear_console()
        download_animation()
    elif user_input == 8:
        clear_console()
        print("\t\t 1.Check Balance")
        print("\t\t 2.Request Statement")
        print("\t\t 3.Change PIN")

        bkashInput = int(input("Choose one: "))
        if bkashInput == 1:
            clear_console()
            pin = int(input("Enter Your PIN: "))
            if pin == user_pin:
                clear_console()
                print("Your current balance is: ", balance)
        elif bkashInput == 2:
            clear_console()
            pin = int(input("Enter Menu Pin: "))
            if pin == user_pin:
                clear_console()
                print("9/1/2023 Mobile Recharge 29tk")
                print("9/7/2023 Mobile Recharge 49tk")
                print("9/12/2023 Cash Out 2000tk")
                print("9/15/2023 Pay Bill 1500tk")
                print("9/25/2023 Mobile Recharge 290tk")
        elif bkashInput == 3:
            clear_console()
            NationalId = int(input("\t\t Enter Your National Id Number:"))
    elif user_input == 9:
        clear_console()
        NationalId = int(input("\t\t Enter Your National Id Number:"))
        reset_pin()

    else:
        print("You Entered Wrong Number😥")