a = int(input("введите a :"))
b = int(input("введите b :"))
if a==0:
	if b ==0:
		print("x любое")
	else:
		print("нет решений")
else:
	c = b/a 
	if a>0:
		print("x>c")
	else:
		print("x<c")
			