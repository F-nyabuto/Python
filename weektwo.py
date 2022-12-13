import math

# File name: All lowercase or under score
#This is comment

#print("Hello world")

#x = 1
# print(type(x))
# print(id(x))

#x = "changed"
# print(type(x))
# print(id(x))


#X = 5
#print(x + X)
#print(x, X)

# print(X)

#y, z = "variable", "one"
#print(y + " " + z)

'''
write anything
as a comment
'''

#print("Python \" programming")
#print('Python " programming')
#print("Python \nProgramming")

name = """
This text
is going to be
multiple lines
"""
'''
name = "This text \nisgoing tobe \nmultiple lines"

firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName
print(fullName)

fullName = f"My name is {firstName} {lastName}"

print(fullName)
print(fullName.upper())
print(fullName.title())

print(fullName.find("AME"))

print(len(fullName))  # Get the length of the string with len() method

print(fullName[0])  # Get the index value
print(fullName[-1])  # Get the first index from the end
print(fullName[0:5])  # Slicing: Get the indexes from 0 to 4
print(fullName[:])  # Default zero beginning and length of the variable ending

print(fullName.replace(" ", "-"))  # replacing "space" to "-"
"""
My name is John Doe
01234 
                 -1
"""

# Define a variable name, a variable role, print it as a formatted string saying eg "John is a student"
name = "Sara"
role = "student"
print(f"{name} is a {role}.")


print(bin(52))  # Get binary value
print(hex(52))  # Get hexadecimal represantative


x = 2
y = 45

print(y/x)
print(y//x)
print(y % x)

z = -585.8545
print(round(z))
print(abs(z))

print(math.floor(z))
print(math.ceil(z))

# receive input from the user, It is always string
#age = input("Write your age: ")
#print(f"your age is {age}")
# print(age + 2) #will give us a typeError because adding a str to int is not possible
#print(int(age) + 2)

a = ""
print(bool(a))
'''

d = 8
f = 9
print(d > f)
print(d == f)
print(d != f)
