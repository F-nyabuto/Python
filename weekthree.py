# # if statement
# a = 8
# b = 9
# if a == b:
#     print('a equals b')

# if a == b: print('a equals b') #This one is correct as well


# # Ternary operator:
#print("a equals b") if a == b else print("a is not equal to b")


# age = 68
# if age > 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")


# # And: all conditions should be true in order for the code to be executed
# if (age >= 18) and (age < 65):
#     print("Eligible")


# # Or: If one condition is true the code is going to get executed
# if age < 18 or age > 65:
#     print("Not eligible")


# name = input("Write your name: ")
# if name:
#     print(f"Hi {name}")
#     #print("Hi " + name)
# elif not name:
#     print("You didn't write your name")


# # Practice 1
# number = int(input("Write a number: "))
# if number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


# # Ternary Operator
# print("Even") if number % 2 == 0 else print("Odd")


# # Write a program to check if the last digit of a number entered by user, is divisible by 3 or not
# number = int(input("Write a number: "))
# lastDigit = number % 10
# if lastDigit % 3 != 0 or lastDigit == 0:
#     print("Not divisable to 3")
# else:
#     print("Divisable to three")


# # loop through strings
# for x in "Python":
#     print(x)


# # loop through numbers
# for x in range(5):
#     print(x)


# # print even numbers from 2 to 10 , range(startNumber->default is 0, EndingNumber(not included), step->default is 1)
# for x in range(2, 11, 2):
#     print(x)


# print(type(range(5)))


# # loop through lists
# i = [0, 1, 2, 3, 4, ]
# for x in i:
#     print(x)


# # Break
# names = ["Sara", "John", "Leo"]
# for name in names:
#     if name == "sara":
#         print("sara is in names list")
#         break
# else:
#     print("sara not found")


# # Continue
# for x in range(4):
#     if x == 1:
#         continue
#     print(x)


# # While loops
# i = 1
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
#     #i = i+1


# # CONTINUE IN WHILE LOOPS
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# # NEXT CODE IS INCORRECT AND WILL RUN FOREVER
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         continue
#     i += 1


# # Find sum of numbers from a list, using while loop.
# myList = [1, 5, 8]
# sum = 0
# i = 0
# while i < len(myList):
#     sum += myList[i]
#     i += 1
# print(sum)


# # While else Guessing
# guess = 0
# answer = 8
# while answer != guess:
#     guess = int(input("Guess a number: "))
# else:
#     print("you guessed right")


# # NESTED LOOPS
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)
#print(i, end=' ')


# # PRACTICE 4
# row = 5
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print('')
