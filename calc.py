import math
print("InfinityOS Calculator Version 1.0")
print("Available operations: +,-,*,/,^")
running = True
while running:
	Num_A = input("Enter number A: ")
	Num_B = input("Enter number B: ")
	Operation = input("Enter operation (+ - * / ^): ")
	if Operation == "+":
		result = int(Num_A) + int(Num_B)
	elif Operation == "-":
		result = int(Num_A) - int(Num_B)
	elif Operation == "*":
		result = int(Num_A) * int(Num_B)
	elif Operation == "/":
		result = int(Num_A) / int(Num_B)
	elif Operation == "^":
		result = math.pow(int(Num_A), int(Num_B))
	else:
		print("Wrong operation.")
	if Num_A == "exit" or Num_B == "exit" or Operation == "exit":
		break
		exit()
	print(f"Result is: {result}")