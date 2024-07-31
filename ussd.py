# A USSD Banking program

balance = 10000.00
amount = int(input("Enter an amount: "))
action = input("What do you want to do?")



   
def deposit():  #Deposit function defination
        credit = balance + amount
        print(credit)


def transfer():    # Transfer function defination
        transfer_balance = balance - amount
        print(transfer_balance)
    

def withdrawal():    ## Withdrawal Function defination
        debit = balance - amount
        print(debit)

    

def check_balance():  ## Check balance function defination.
        account = balance
        print(account) 

if action == "deposit":
        deposit()

elif action == "withdrawal":
        withdrawal()

elif action == "transfer":
        transfer()

else:
        check_balance()

