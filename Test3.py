# Pre-Test
# Task 1
import random

twentysix = [random.randint(1, 5) for a in range(26)]
my_list = []
print(twentysix)

for n in range(len(twentysix)):
    if n > 0:
        my_list.append(twentysix[n] + my_list[n-1])
    else:
        my_list.append(twentysix[n])
for a in my_list:
    print(a)