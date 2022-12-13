#Write a progrm to print the following patter using a loop
'''
1
12
123
1234
12345
'''

biz1 = ["1"]
biz2 = ["1 2"]
biz3 = ["1 2 3"]
biz4 = ["1 2 3 4"]
biz5 = ["1 2 3 4 5"]

for x in biz1:
    print(x)
    for x in biz2:
        print(x)
        for x in biz3:
            print(x)
            for x in biz4:
                print(x)
                for x in biz5:
                    print(x)


                    break

# _____________________correction_____________
row = 7
i = 0
for i in range(1, row + 1):
    for j in range(1, i):
        print(j, end = ' ')
    print(' ')


