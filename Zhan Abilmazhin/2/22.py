a = int(input("значение a :"))
b = int(input("значение b :"))
c = int(input("значение с :"))
x = int(input("значение x :"))
y = int(input("значение y :"))
if a>b:
	r =a;a=b;b=r 
if b>c:
	r=b;b=c;c=r
if a>b:
	r=a;a=b;b=r
if x>y:
	r=x;x=y;y=r 
if a<x and b<y:
	print("пройдет")
else:
	print("не пройдет")