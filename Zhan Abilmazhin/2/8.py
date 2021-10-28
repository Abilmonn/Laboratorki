a = int(input("цена продукта (а) : "))
b = int(input("количество продуктов (b) : "))

s = a*b
if s>500:
	s = s * 0.9
	print(s)
else:
	print(s)