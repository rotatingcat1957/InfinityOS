import os
import platform
import socket
from time import strftime

current_os = platform.system()

with open("user_data/username.txt", "r") as f:
	username = f.readline()

print(f"Welcome to InfinityOS v1.22, {username}\n\nCurrent date and time is: {strftime("%H:%M:%S %p ") + strftime("%y-%m-%d")}\n\nYour current OS: {current_os}\n\nCurrent hostname: {socket.gethostname()}\n\nIP Address: {socket.gethostbyname(socket.gethostname())}\n")

running = True

while running:
	dirname = os.path.abspath(os.getcwd())

	main = input(f"{dirname}> ")

	if main == "help":
		print("""
		List of available commands:

		expunge - Deletes a file.
		
		expdir - Deletes a folder/tree.
		
		cd - Moves up or down a folder.
		
		cp - Copies files to directories and/or directories to directories. (Creates new directory if doesn't exist & if you want to)

		ls - Lists all current files and directories.
		
		move - Moves a file. (To move do mv, example.txt, example/)

		ren - Renames a file.
		
		read - Reads a file. (to read a file do read, example.txt)
		
		help - Lists all current commands within the OS itself.
		
		pwd - Types out/prints current working directory.
		
		cls - Clears the screen.

		run - Runs inputted file.

		makedir - Creates folders (for example makedir then ExampleFolder/)
		
		info - Info about system (version, hostname, etc etc)
		
		calc - Calculator.
		
		browse - Internet browser.

		vi - Text editor.

		echo <text you want to input> - Echoes the text you
		input to the command. (for date and time do echo #date or echo #time)
		
		ping <website> [packets] - Pings the IP or site you input with the amount
		of packets you enter. (Example: ping, 8.8.8.8, 16)
		
		passwd - Changes password based on your input.
		
		usrname - Changes username based on your input.
		
		whoami - Displays current user.
		
		whatismypassword - Displays current password.
			""")
	elif main == "expunge":
		file_to_delete = input("Enter filename to delete (be careful not to destroy your OS): ")
		if current_os == "Windows":
			os.system(f"del {file_to_delete}")
		else:
			os.system(f"rm {file_to_delete}")

	elif main == "expdir":
		folder_to_delete = input("Enter foldername to delete (be careful not to destroy your OS): ")
		if current_os == "Windows":
			os.system(f"rd {folder_to_delete}")
		else:
			os.system(f"rm {folder_to_delete}")

	elif main == "makedir":
		folder_to_create = input("Enter folder to create: ")
		os.system(f"mkdir {folder_to_create}")

	elif main == "cd":
		change_folder = input("Enter folder to move into: ")
		if os.path.exists(change_folder):
			os.chdir(change_folder)
		else:
			print("Folder not found.")

	elif main == "vi":
		if current_os == "Windows":
			os.startfile("vi.py")
		else:
			os.system("python3 vi.py")

	elif main == "browse":
		if current_os == "Windows":
			os.startfile("browser.py")
		else:
			os.system("python3 browser.py")

	elif main == "ls":
		dir_to_list = input("Enter directory to list: ")
		if current_os == "Windows":
			os.system(f"dir {dir_to_list}")
		else:
			os.system(f"ls {dir_to_list}")

	elif main == "move":
		file_to_move = input("Enter file to move: ")
		foldername = input("Enter folder name to move file into: ")
		if os.path.exists(foldername):
			os.system(f"move {file_to_move} {foldername}/")
		else:
			print("Folder not found.")

	elif main == "ren":
		file_to_rename = input("Enter file to rename: ")
		new_name = input("Enter new name of file: ")
		if current_os == "Windows":
			os.system(f"rename {file_to_rename} {new_name}")
		else:
			os.system(f"mv {file_to_rename} {new_name}")

	elif main == "read":
		file_to_read = input("Enter file to read: ")
		if current_os == "Windows":
			os.system(f"type {file_to_read}")
		else:
			os.system(f"cat {file_to_read}")

	elif main == "cp":
		file_to_copy = input("Enter filename to copy: ")
		dir_to_copy_into = input("Enter directory name to copy file into: ")
		if os.path.exists(dir_to_copy_into):
			if current_os == "Windows":
				os.system(f"copy {file_to_copy} {dir_to_copy_into}")
				print("OK. Copied file(s).")
			else:
				os.system(f"cp {file_to_copy} {dir_to_copy_into}")
				print("OK. Copied file(s).")
		else:
			question = input("Directory doesn't exist. Do you want to create it first? (Yes/No): ")
			if question == "Yes" or "yes" or "YES" or "y" or "Y":
				os.system(f"mkdir {dir_to_copy_into}")
			elif question == "No" or "no" or "NO" or "n" or "N":
				print("OK. No files copied and no directories made.")
			else:
				print("Wrong question. Available: Yes/No.")

	elif main == "pwd":
		if current_os == "Windows":
			os.system("cd")
		else:
			os.system("pwd")

	elif main == "cls":
		if current_os == "Windows":
			os.system("cls")
		else:
			os.system("clear")

	elif main == "run":
		file_to_run = input("Enter file to run: ")
		if current_os == "Windows":
			os.system(f"{file_to_run}")
		else:
			os.sytem(f"{file_to_run}")

	elif main == "info":
		print(f"""
		OS Type: {current_os},
		Architecture: {platform.machine()},
		System name: {socket.gethostname()},
		Platform info: {platform.platform()}
			""")

	elif main == "whoami":
		print(f"Your current username: {username}")

	elif main == "whatismypassword":
		with open("user_data/password.txt", "r") as f:
			password = f.readline().strip()
		print(f"Your current password: {password}")

	elif main == "usrname":
		new_username = input("Please enter new username: ")
		with open("user_data/username.txt", "w") as f:
			f.truncate()
			f.writelines(new_username)

	elif main == "passwd":
		new_password = input("Please enter new password: ")
		with open("user_data/password.txt", "w") as f:
			f.truncate()
			f.writelines(new_password)

	elif main == "echo":
		echo_text = input("Enter text to echo out: ")
		if echo_text == "#time":
			print(strftime("%H:%M:%S %p"))
		elif echo_text == "#date":
			print(strftime("%y-%m-%d"))
		else:
			print(f"{echo_text}\n")

	elif main == "calc":
		if current_os == "Windows":
			os.startfile("calc.py")
		else:
			os.system("python3 calc.py")

	elif main == "ping":
		address_to_ping = input("Enter IP address/URL: ")
		packets = input("Enter packet amount: ")
		if current_os == "Windows":
			os.system(f"ping {address_to_ping} /n {packets}")
		else:
			os.system(f"ping {address_to_ping} {packets}")

	elif main == "exit":
		break
		exit()

	else:
		print("Wrong Command.")