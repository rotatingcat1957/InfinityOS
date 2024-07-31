import os
import time
path_to_setup = r"setup.py"
print("InfinityOS Loading...")
loader = ["\\","-","/","|"]
for i in range(4):
	for j in range(4):
		print(loader[j], end="\r", flush=True)
		time.sleep(0.25)
print("Starting Setup...")
if os.path.exists(path_to_setup):
	print("File/path exists.")
	os.startfile(path_to_setup)
	exit()
else:
	print("File/path doesn't exist. Try to create it first.")
	input("\r")
	exit()