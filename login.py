import os
from time import strftime
print(f"Time Is: {strftime("%H:%M:%S %p")}, date is: {strftime("%y-%m-%d")}")
with open("user_data/username.txt", "r") as f:
    username = f.readline().strip()
print(f"Hello, {username}")
loginPass = input("Enter your password: ")
with open("user_data/password.txt", "r") as f:
	actual_password = f.readline().strip()
if loginPass == actual_password:
	os.startfile("home.py")
	exit()
else:
	input("Wrong Password!")