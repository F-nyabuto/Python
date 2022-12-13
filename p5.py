'''
FUNCTIONS
- A block of code that



#Function
def functionName():
    print("This function will be printed")
functionName()#- We call the function to be excecuted. Otherwise, the code will not be executed

def getAge(name, age):
    print(f"You are {name} and {age} years old")
    getAge("Felix", 12)
#Parameters are the variables passed to the function

def color(red, green, yellow):
    print(f"Red{red}, Green{green}, Yellow{yellow}")
color(green = "Tree", Yellow = "Banana", Red = "Rose")


def numSum(*list):
    total = 0
    for num in list:
       # total = total + num
        total += num
    return total

print(numSum(2, 8, 1))

message = "a" #Global variable

def send():
    message = "2" # Local variable

    print(message)

send()

'''


















