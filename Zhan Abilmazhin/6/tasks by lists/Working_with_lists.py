element = []
for i in range(1,6):
	new = int(input("введите элементы : "))
	element.append(new)

l = []
l.append([5,-6])
l.append(element)
l.sort()
print(l)  
