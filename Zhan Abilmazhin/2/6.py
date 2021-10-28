import math
a = int(input("число a : "))
b = int(input("число b : "))
c = int(input("число c : "))

D = b **2 -4*a*c 
if D>=0:
	x1 = (-b-math.sqrt(D))/(2*a)
	x2 = (-b+math.sqrt(D))/(2*a)
	print(x1,x2)
else:
	print("нет решения")