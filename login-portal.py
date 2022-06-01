import os
print("WELCOME TO REGISTER AND LOGIN PORTAL")
welcome = input("Do you have an account (Yes/No): ")

if welcome == "No":
    while True:
        username = input("Enter your desired username here: ")
        password = input("Enter your password here: ")
        password2 = input("Confirm password: ")
        
        if password == password2:
            file = open(username +  ".txt","w")
            file.write(username + ","  + password)
            file.close()
            print("Account creation successful")
            break
        else:
            print("password does not match. Try again")


if welcome == "Yes":
    while True:
        login1 = input("Enter your username here: ")
        login2 = input("Enter your password here: ")
        if os.path.exists(login1 + ".txt"):
            file = open(login1 + ".txt","r")
            data = file.readline()
            file.close()
            if data == login1 + "," + login2:
                print("Welcome " + login1)
                break
            else:
                print("Incorrect password. Try again")
        else:
            print("This account does not exist, sign up for a new account.")