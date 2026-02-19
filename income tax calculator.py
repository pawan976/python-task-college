income = float(input("enter annual: "))
age = int(input("enter age: "))
if age>=60:
    exemption = 300000
else:
    exemption = 250000
tax = 0
if income <= exemption:
    tax = 0
elif income <= 500000:
    tax = (income - exemption)*0.05
elif income <= 1000000:
    tax = (income - exemption)*0.05+(income - 500000)*0.20
else:
    tax = (500000 - exemption)*0.05+(10000000 - 500000)*0.20+(income-1000000)*0.30
print("Income tax =",tax)