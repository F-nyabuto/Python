#-------------------------------- IF STATEMENTS--------------------------------------------------
'''
If statements notes
format:
        if condition:
            code to be executed
**the identation indicates the code block. i.e whatever is indented after the if statement is what will be executed.**


elif statements notes
        if a == b:
            code to be executed
        elif a > b:
            code to be executed

else statement
-> If none of preceding conditions is true, this one will be executed.


$If you have one statenebt foor if and one for else, you can put them all in one statement.$
#read on ternary operator
Ternary operator take the following format:
print("Condition if statement 1 is fulfilled") if (condition 1) else print("statement 2 if condition 1 is not fulfilled")



'''


#------------classroom example one-------------------
#a = 8
#b = 8

#if a == b:
#    print("a equals b")
#line 20
#if a == b: print("A is equal to B") else: print("A is not equal to B")
#Example two- using elif and else

#age = int(input("Enter your age: "))
#if age > 100:
#    print("Ancestor")
#elif age > 18:
#    print("Adult")
#elif age >=13:
#    print("Teenager")
#elif age >= 5:
#    print("Child")
#else:
#    print("Baby")



#__________________________________LOGICAL OPERATORS__________________________________
'''
and
-used to combine conditional statements.
-Executed when ALL the conditionals are true

or
-usd to combine conditional statements when at least one of them is true.

not
-reverses the result of the expression in front of it.

pass
if statements cannot be empty.

Loops
1. for
- used for iterating over a sequence of any object that is iterable. That ie either a list, tuple,set or string.
        for x in "Python"
            print(x)
$Indentation specifies a block of code to be executed within  the for loop.$


2. Break
-break statement is used to jump out of a loop for performance reasons. The loop will be stopped before it has gone through all items if the item
wanted has been found.


3. For else

4. Continue
-with continue statement, we can stop the current iteration of the loop and continue with the next.

5. while loops
-with the while loop, we can execute a set of statements as long as a condition is true.

6/ Nested loops
- a nested loop is a loop within a loop.
- The inner loop will be executed one at a time for each iteration of the outer loop.
'''
#Examples using logical operators
#age = 65

#and
#if (age >= 18) and (age < 68):
#    print("Eligible")

#or
#if (age >= 18) or (age < 68):
#    print("Not eligible")

#not
#name = input("Enter your name: ")
#if name:
#    print(f"Hi {name}") #Equivalent to concatenation. Ie same as this line: print("Hi " + name)
#    #pass
#    pass
#elif not name:
#    print("You did not enter any name.")


#for loop
#for x in "Python":
#    print(x)

#for x in range(2, 11, 3):# this code will print 2,(2+5=5), (5+3=8)
#    print(x)

#loop through lists
#i = [0, 1, 2, 3, 4, ]
#for x in i:
#    print(x)


#$range usually start from 0. But we can specify as shown here| range(2, 8)| This code will print numbers from 2 to 7$



#Break

#names = ["Sara, Felix, Sharon, Kevin, Maria, Collins"]

#for name in names:
#    if name == "Sara":
#        print("Sara has been found")
#        break


#while loops

'''i = 1
while i < 6:
    print(i)
    if i == 5:
        continue
    i += 1'''


#nested loops
adj = []
fruits = []
