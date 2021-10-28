 
#1
print ('Python work!')

#2
num=5
print (num)

#3
print("Comment me :)")
# print("Comment me :)")

#4
number = 2
print(number ** 3)

#5
getSix = 1467 // 6
print(getSix)

#6
string = "Data"
mult = string * 4
print(mult)

#7
number = int(input("введите число :"))
if number % 2 == 0:
	print("Yes")

#8
i = 4
while i <= 13:
 if i != 7 and i != 11:
 print(i ** 2)

 i += 1

 #9
 a = input("Введите число: ")
 n1 = int(a)
 n2 = int(a * 2)
 print (n1 + n2) #можно сделать короче a = int(input("введите число :"))
 										#print((a*2)+a)

#10
Результат:
num = 46
word = "string"
word *= 5
print(num)
print(word)

#11
x = 5 
symbol = 'F' 
word = "Привет" 
d = 90.2 
CONST = 67
print(word)

#12
number = int(input("Введите число с 4 цифрами: "))
n1 = round(number // 1000 % 10) 
n2 = round(number // 100 % 10) 
n3 = round(number // 10 % 10) 
n4 = round(number % 10)
print(n1, ",", n2, ",", n3, ",", n4)

#13
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
age = input("Ваш возраст: ")
print (name + " " + surname + ". Ваш возраст: " + age)

#14
friend_name = input("Как зовут вашего друга? ")
print("Вашего друга зовут - ", friend_name)

#15
print(136 // 7)

#16
num_1 = int (input ("Введите 1 число: "))
num_2 = int (input ("Введите 2 число: "))
num_3 = int (input ("Введите 3 число: "))
res = num_1 + num_2 + num_3
print ("Добавление чисел: ", res)
res = num_1 - num_2 - num_3
print ("Вычитание чисел: ", res)
print ("Умножение чисел: ", num_1 * num_2 * num_3)
print ("Деление чисел: ", num_1 / num_2 / num_3)
print ("Остаток при делении чисел: ", num_1 % num_2 % num_3)

#17
a = 11
b = 8.23
c = "9.1"
res = float (a) + b + float (c)
print(res)

#18
x = float(input("Введите число: "))
if x < 0:
 print("Это отрицательное число")
elif x == 0:
 print("Число равно нулю")
else:
 print("Это положительное число")

#19
a = input ("Введите число: ")
if a.isalpha():
 print ("Введите числа")
elif a.isdigit():
 print ("Вы ввели число")

 #20
age = int(input ("Сколько вам лет?"))
if age > 18:
 print("Вам уже все можно")
elif age == 18:
 print("Ура, вам 18 лет!")
else:
 print("Вы еще слишком молоды")

#21
x = int(input("Первое число: "))
math = input("Операция: ")
y = int(input("Второе число: "))
if math == '+':
	print(x, " + ", y, " = ", (x + y))
elif math == '-':
 	print(x, " - ", y, " = ", (x - y))
elif math == '*':
 	print(x, " * ", y, " = ", (x * y))
elif math == '/':
 	if y != 0:
 		print(x, " / ", y, " = ", (x / y))
 	else:
 		print("Нельзя делить на ноль!")
else:
 print("Неверная операция")