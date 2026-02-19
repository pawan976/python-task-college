correct_user = "admin"
correct_pass = "1234"

attempt = 0

while attempt < 3:
    user = input("Enter username: ")
    password = input("Enter password: ")

    if user == correct_user and password == correct_pass:
        print("Login successful")
        break
    else:
        attempt += 1
        print("Invalid login! Attempts left:", 3 - attempt)

if attempt == 3:
    print("Account locked due to 3 failed attempts")
