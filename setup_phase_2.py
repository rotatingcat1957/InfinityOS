import os
os.system("cls")
print("""
InfinityOS Python Setup
========================

Please enter the username: \r


""")
username = input("")
os.system("cls")
print("""
InfinityOS Python Setup
========================

Please enter the password: \r


		""")
password = input("")
with open("user_data/username.txt", "w") as f:
	f.writelines(username)
with open("user_data/password.txt", "w") as f:
	f.writelines(password)
input("")
os.startfile("main.py")
exit()