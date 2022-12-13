# Practice 5 of week 3
# Write a program using for loop to print the following reverse number pattern.
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# n = 5
# k = 5

# for i in range(0, n+1):
#     for j in range(k-i, 0, -1):
#         print(j, end=' ')
#     print()

# def functionName():
#     print("This function is executed")


# functionName()

# def getUser(name, age):
#     print(f"You are {name} and {age} years old")


# getUser("Sam", 12)
# Parameters are the variables passed to the function
# Arguments are the values passed to the function

# kwargs
# def color(red, green, yellow):
#     print(f"Red {red}, Green {green}, Yellow {yellow}")


# color(green="tree", yellow="banana", red="rose")

# default parameter value
# def increment(number, by=1):
#     print(number, number + by)


# print(increment(5))
# print(increment(5, -2))
# functions return none value by default


# *args
# def getList(*list):
#     print(list)


# getList(1, 5, 8)


# def identify(*user):
#     for i in user:
#         print(f"user is {i}")


# identify("John", "Ema")


# create a function that receives a list numbers and returns the sum of them

# def numSum(*list):
#     total = 0
#     for num in list:
#         # total = total + num
#         total += num

#     return total

# print(numSum(2, 8, 1))
# first loop 0+2 , second time 2 + 8, third 10 + 1


# Practice 1
# def multiply(*list):
#     total = 1
#     for num in list:
#         # total = total * num
#         total *= num

#     return total


# print(multiply(5, 8, 2))


# **kwargs
# def save_user(**user):
#     return(user)


# def user_id(**user):
#     return(user['id'])


# print(save_user(id=5, name="Sam", job="Fire fighter"))
# print(user_id(id=5, name="Sam", job="Fire fighter"))


# Practice 2
# [1, 1, 2, 2, 1 ,3] -> [1, 2, 3]
# a.append(x) to add x to list a

# def getUnique(list):
#     unique = []
#     for i in list:
#         if i not in unique:
#             unique.append(i)

#     return unique


# print(getUnique([2, 5, 5, 2, 7]))


# GLOBAL AND LOCAL VAIABLES
# message = "a"  # Global variable


# def send():
#     message = "Z"  # Local variable
#     print(message)

# send()

# def receive():
#     global message
#     # we can change global variables in functions with "global" keyword BUT IT's A BAD PACTICE
#     message = "Z"
#     return message


# receive()
# print(message)

# input % 3 == 0

# Practice 3 FizzBuzz
# def fizz_buzz(input):
#     if (input % 3 == 0) & (input % 5 == 0):
#         return "FizzBuzz"
#     elif input % 3 == 0:
#         return "Fizz"
#     elif input % 5 == 0:
#         return "Buzz"
#     else:
#         return input

# print(fizz_buzz(4))


# VSCode Shortcuts:
# shift + end (for windows) function key + right arrow (for mac )-> end of the line
# shift + home (for windows) function key + left arrow (for mac )-> beginning of the line

# shift + pgdn (for windows) -> ending of the file
# shift + pgup (for windows) > beginning of the file

# shift + arrow keys to select lines
# alt + arrow keys to move the lines

# shift + alt + arrow keys  to copy the line

# ctrl + / (on windows) command + / (on mac)->converts to comment

# Create a function to remove the first n characters from a string
# e.g. -> ("python", 2) returns "thon"


# def removeChars(word, n):
#     slicedWord = word[n:]
#     return slicedWord

# print(removeChars("Elementary programming", 3))


# Define a function to get a list as parameter
# and checks if the first and last element are the same


def same(list):

    firstNum = list[0]
    lastNum = list[-1]

    if firstNum == lastNum:
        return True
    else:
        return False


print(same([1, 2, 5, 1]))
