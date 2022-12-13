"""
File handling in python
"""

"""# Create a file object
my_file = open("C:\\Users\\Nyabu\\Desktop\\python.txt", "r")


# read a file
print(my_file.read())

# read a line in a txt file
print(my_file.readline())
"""
my_file = open("C:\\Users\\Nyabu\\Desktop\\python.txt", "a")# The previous content is not deleted in the code
my_file.write("\nThis is a new line of text in my file")


my_file = open("C:\\Users\\Nyabu\\Desktop\\python.txt", "w")# Deletes the previous content
my_file.write("\nThis is my second new line of text in my file")



# Closing a file in python -> Always close your files using close() after
my_file.close()
print(my_file.closed)


# Creating a new file

