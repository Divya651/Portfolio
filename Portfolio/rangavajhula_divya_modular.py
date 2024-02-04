import math
import random

radius = int(input("Please enter the radius of the sphere: "))

volume = 4/3 * math.pi * pow(radius, 3)

print("the volume of the sphere with radius of", radius, "is", volume)

random_number = random.randint(1,10)

factoral_variable = math.factorial(random_number)

print("The factorial of", random_number, "is", factoral_variable)