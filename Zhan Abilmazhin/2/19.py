st = int(input("введите стаж работы :"))
if st < 5:
	zp = 130
elif st <= 15:
	zp = 180
else:
	zp=180+(st-15)*10
print(zp)