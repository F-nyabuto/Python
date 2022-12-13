# #Practice 1
# '''
# Write a class named circle
# Constructed by a radius
# Has a method to compute the area
# Has a method to construct the perimeter
# '''
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def areaFunction(self):
#         area = ((22/7) * self.radius ** 2)
#         print(f"The area of a circle of radius {self.radius} is {area}")
#
#     def perimFunction(self):
#         perimeter = ((22/7) *2 * self.radius)
#         print(f"The perimeter of a circle of radius {self.radius} is {perimeter}")
#
#
# rad1 = Circle(10)
# rad1.areaFunction()
# rad1.perimFunction()


# practice 2
"""
Create a food class with name, calories attributes
Define a function named Kcal and divide calories by 1000

Create a vegetable class which inherits everything from the food class
Give the calories attribute a default value 0
Redefine the Kcal method and add 10 to the final result of this method
"""


class Food:
    def __int__(self, name, calories):
        self.name = name
        self.calories = calories

    def kcal(self):
        cal = self.calories / 1000
        print(f"K-Calories are: {cal}")


class Vegetable(Food):

    cal = 0
    print(f"K-Calories are: {cal}")


x = Vegetable("banana", 100)
x.kcalcal = self.calories / 1000
        print(f"K-Calories are: {cal}")()
