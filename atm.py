balance=5000
def check_balance(balance):
    print(f"Your Account Balance is={balance}")
    return balance
def deposite(balance):
    try:
        amount=int(input("Enter your deposite Amount="))
    except:
        print("Please give numberical value")
        return balance
    if amount<0:
        print("Negative Amount Can't Deposite")
        return balance
    else:
        balance=balance+amount
        print("Your amount is succesfully deposited")
        return balance
def withdraw(balance):
    try:
        withdraw_amount=int(input("Enter your withdrawn amount="))
    except:
        print("Please give numerical value")
        return balance
    if withdraw_amount>balance or withdraw_amount<0:
        print("Insufficient Balance")
        return balance
    else:
        balance=balance-withdraw_amount
        print("Your Withdrawal is successfull")
        return balance
def menu():
    print("=============== Menu ===============")
    print("Your Options:-")
    print("1.Check Balance","\n2.Withdraw","\n3.Deposite","\n4.Exit")





while True:
    menu()
    choice=input("Enter your Choice=")
    choice1=choice.strip().upper()
    if choice1=="CHECK BALANCE" or choice1=="1":
        balance=check_balance(balance)
    elif choice1=="DEPOSITE" or choice1=="3":
        balance=deposite(balance)
    elif choice1=="WITHDRAW" or choice1=="2":
        balance=withdraw(balance)
    elif choice1=="EXIT" or choice1=="4":
        print("Thanks You \nVisit Again!")
        break
    else:
        print("Wrong Input \nPlease Correct Input Speeling")
