a = int(input("значение а: "))
b = int(input("значение b: "))
while True:
	if a == b:
		print(a)
		break
	elif a >b:
		a = a-b
	else:
		b = b-a