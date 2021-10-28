q = float(input("введи q : "))
s = 0
i = 1
while True:
	s = s + i
	i = i + 1
	if s>q:
		print(i-2)
		break