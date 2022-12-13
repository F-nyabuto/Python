#Find sum of numbers from a list using while loop

numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0
i = 0
while i<(len(numbers)):
    sum += numbers[i]
    i += 1

print(sum)

'''guess = 0
answer = 8

while answer != guess:
    guess = int(input("Make your guess: "))
else:
    print("Your guess was correct")'''