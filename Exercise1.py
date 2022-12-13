#write a program to check if the number entered by a user is odd or even.

num = int(input("Enter a number: "))
#checking if the number is even
mod = num % 2

if mod == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#using ternary operator
print("The number is even") if mod == 0 else print("The number is odd")
