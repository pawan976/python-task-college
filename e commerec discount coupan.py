cart = float(input("Enter cart value: "))
member = input("Membership (silver/gold/platinum): ")
festival = input("Festival season? (yes/no): ")

discount = 0

# membership discount
if member.lower() == "silver":
    discount = 5
elif member.lower() == "gold":
    discount = 10
elif member.lower() == "platinum":
    discount = 15

# cart value discount
if cart > 5000:
    discount = max(discount, 20)
elif cart > 2000:
    discount = max(discount, 10)

# festival discount
if festival.lower() == "yes":
    discount = max(discount, 25)

final_amount = cart - (cart * discount / 100)

print("Highest discount applied:", discount, "%")
print("Final payable amount:", final_amount)
