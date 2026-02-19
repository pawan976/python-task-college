rating = int(input("Performance rating (1-5): "))
exp = int(input("Years of experience: "))
attendance = float(input("Attendance percentage: "))

increment = 0

if rating == 5:
    increment += 20
elif rating == 4:
    increment += 15
elif rating == 3:
    increment += 10
else:
    increment += 5

if exp > 5:
    increment += 5

if attendance > 90:
    increment += 3

print("Total increment =", increment, "%")
