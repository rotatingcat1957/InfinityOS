import os
import platform
opsys = platform.system()
print("""
InfinityOS Python Setup
========================

	Welcome to Setup.

	This portion of the Setup program prepares InfinityOS
	Python to run on your computer.

	・ To set up InfinityOS now, type 1 and press ENTER.

	・ To quit Setup without installing InfinityOS, type 2
	  and press ENTER.


[   1=Continue  2=Quit                        ]
	""")
select_option = input(":")
if select_option == "1":
	if os.path.exists("setup_phase_2.py"):
		os.startfile("setup_phase_2.py")
	else:
		input("File setup_phase_2.py doesn't exist.")
		exit()
if select_option == "2":
	print("""
	InfinityOS Python Setup
	========================
	
	Changes haven't been made to your computer.
	You may now quit this process.
	Press any key to exit...
		""")
	input("")
	os.startfile("main.py")
	exit()