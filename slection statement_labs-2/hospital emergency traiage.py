age = int(input("Enter age: "))
heart = input("Heart rate abnormal? (yes/no): ")
injury = input("Severe injury? (yes/no): ")

if heart.lower() == "yes" or injury.lower() == "yes":
    print("Priority: CRITICAL")

elif age > 65:
    print("Priority upgraded to MODERATE (Senior citizen)")

else:
    condition = input("Enter condition (moderate/normal): ")
    if condition.lower() == "moderate" and age > 65:
        print("Priority upgraded to CRITICAL")
    elif condition.lower() == "moderate":
        print("Priority: MODERATE")
    else:
        print("Priority: NORMAL")
