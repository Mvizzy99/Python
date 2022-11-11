# By Matthew Visentine
# Credit to "ENGR 102: Engineering Lab I Computation" Published by zyBooks for inspiration
# 9/27/22

from math import *

num = int(input("Enter a positive integer: "))
iterations = 0

print(f"The Juggler sequence starting at {num} is:")

#Iterate until num = 1, printing as it goes without line breaks
while num != 1:
    print(num, end = ", ")
    if num % 2 == 0:
        num = floor(sqrt(num))
    else:
        num = floor(sqrt(num ** 3))
    iterations += 1

print(f"1\nIt took {iterations} iterations to reach 1")
