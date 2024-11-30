# Displaying the sentence Login Conformation at the center
import webbrowser as wb
print(" \n                                                        Login Conformation")

# Getting the email ID and password from the user as input 
email = input(" Enter your email: ")
password = input(" Enter your password: ")

# Check if the email and password match your database or some pre-set values
if email == "yourname@gmail.com" and password == "12345678":
    print(" Login successful! \n ")
    
    try:
        with open("responce.txt", "r") as file:
            print(file.read())
            wb.open_new("www.google.com")


    except Exception as e:
        print(e)
        
else:
    print(" Incorrect email or password. Please try again.")
    wb.open_new("www.google.com")
