balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw > balance:
    print("Insufficient balance")

elif withdraw > 50000:
    print("Daily withdrawal limit exceeded")

elif withdraw > atm_cash:
    print("ATM has insufficient cash")

else:
    print("Withdrawal successful")
    balance = balance - withdraw
    print("Remaining balance =", balance)
