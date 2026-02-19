credit = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
existing = float(input("Existing loan amount: "))

if credit < 600:
    print("Loan Rejected: Low credit score")

elif credit >= 750:
    print("Loan Approved")

else:  # 600-750
    if income < 30000 and existing > 500000:
        print("Loan Rejected: Low income & high existing loan")
    else:
        print("Loan Approved after checks")
