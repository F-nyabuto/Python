"""
Nyabuto Felix Ombati
F72YCL
11/04/2022
"""

name = input("Type your name: ").strip()
try:
    year = int(input("What year were you born? "))

    j = ''
    for x in j:
        if year <= 1000:
            print("Type a year with at least 4 integers.")
        elif year >= 10000:
            print("Type a year with no more than four integers.")

except ValueError:
    print("Year of birth must be an integer with four characters. example 2001.")

origin = input("What's your country of origin? ")
print(f'Welcome {name}, you were born in {year} and you are from {origin}')

# part 2
my_file = open("C:\\Users\\Nyabu\\Desktop\\names.txt", "a")  # The previous content in the file is not deleted


def wrt():  # This function writes to the names file
    my_file.write(f"\n {name}, {year}, {origin} ")


wrt()

print("Your information has been updated in the names text file. 😊")
