numbers = input("Input numbers: ")
numbers_list = numbers.split(" ")
print(numbers_list)
numbers_list = [int(i) for i in numbers_list]
print(numbers_list)
a = 0
for i in numbers_list:
    a = a + i
result = a / len(numbers_list)
print(result)