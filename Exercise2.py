# #A program to check if a number is divisible by 5 or not
#
# num = int(input("Enter a number: "))
#
# #divisibility test
# mod = num % 5
#
# if mod == 0:
#     print("The number is divisible by 5. ")
# else:
#     print("The number is NOT divisible by 5. ")
#
# #using ternary operator
# print("Divisible by 5") if mod == 0 else print("Not divisible")
#
#
# x = 1 # int
# y = 2.8 # float
# z = 1j # complex
#
# #convert from int to float:
# a = float(x)
#
# #convert from float to int:
# b = int(y)
#
# #convert from int to complex:
# c = complex(x)
#
# print(a)
# print(b)
# print(c)
#
# print(type(a))
# print(type(b))
# print(type(c))


def square(number):
    return number * number


num = int(input("Type a number: "))
print(square(num))