
# Nyabuto Felix Ombati
'''
Practice 5:
Write a program using for loop to print the following reverse number pattern.
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

rows = 5
i = 0
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print('')

def color(red, green, yellow):
    print(f"Red{red}, Green{green}, Yellow{yellow}")
    
color(green = "Tree", Yellow = "Banana", Red = "Rose")