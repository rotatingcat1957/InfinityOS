import os
import time
print("InfinityOS Loading...")
loader = ["\\","-","/","|"]
for i in range(4):
	for j in range(4):
		print(loader[j], end="\r", flush=True)
		time.sleep(0.25)
print("OK")
os.startfile("login.py")
exit()