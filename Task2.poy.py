# Pre-Test
# Task 1
import random
import os

while True:
    low = int(input("Type the lower bound: "))
    try:
        if low <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Type a value between 1 and 3")


while True:
    upper = int(input("Type the upper bound: "))
    try:
        if upper <= 5:
            break
        else:
            raise ValueError
    except ValueError:
        print("Type a value between 3 and 5")

twentysix = [random.randint(low, upper) for a in range(26)]
my_list = []
print(twentysix)

for n in range(len(twentysix)):
    if n > 0:
        my_list.append(twentysix[n] + my_list[n - 1])
    else:
        my_list.append(twentysix[n])
for a in my_list:
    print(a)


def task_three():
    for i in range(len(my_list)):
        for r in my_list:
            print(f"{r}: {'-' * r}\\{'Skier' if r == my_list[i] else''}")
        os.system('cls')


task_three()
input("Press enter to start skiing.")