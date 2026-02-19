amount = float(input("Enter transaction amount: "))
account_months = int(input("Account age (in months): "))
international = input("Is transaction international (yes/no): ")

if amount > 200000 and account_months < 6 and international.lower() == "yes":
    print("⚠ Suspicious Transaction! Flag for manual verification")
else:
    print("Transaction is normal")
