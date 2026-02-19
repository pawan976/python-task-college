percent = float(input("Enter 12th percentage: "))
maths = input("Studied Maths? (yes/no): ")
entrance = float(input("Entrance exam score: "))

if percent < 75:
    print("Not eligible: Less than 75% in 12th")
elif maths.lower() != "yes":
    print("Not eligible: Mathematics required")
elif entrance < 80:
    print("Not eligible: Entrance score below 80")
else:
    print("🎉 Eligible for admission")
