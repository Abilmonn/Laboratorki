#1
lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]
print(list)

#2
nums = [5, 7, 2, 4, 7, True, "Hello", 6.7, [5, 7]]
nums[0] = 50
nums[5] = 1.01
print(nums[-1][1])

numbers = [5, 2, 7]

numbers.append(100)
numbers.insert(1, True)
b = [5, 6, 8]
numbers.extend(b)

numbers.sort()
numbers.pop(-2)
numbers.remove(6)

#3
nums = [5, 2, 7, "50", False]
for el in nums:
 el *= 2
 print(el)
n = int(input("Enter length: "))
user_list = []
i = 0
while i < n:
 string = "Enter element #" + str(i + 1) + ": "
 user_list.append(input(string))
 i += 1
print(user_list)