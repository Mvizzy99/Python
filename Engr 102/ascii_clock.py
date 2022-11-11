# By Matthew Visentine, Joshua Bohn, Carter Bennett, Braden Goebel
# Credit to "ENGR 102: Engineering Lab I Computation" Published by zyBooks for inspiration
# 10/13/22

#Get input. Add a blank line
user_input = input("Enter the time: ")
print()

#Lay out each number with a list separated by row
zero = ["000", "0 0", "0 0", "0 0", "000"]
one = [" 1 ", "11 ", " 1 ", " 1 ", "111"]
two = ["222", "  2", "222", "2  ", "222"]
three = ["333", "  3", "333", "  3", "333"]
four = ["4 4", "4 4", "444", "  4", "  4"]
five = ["555", "5  ", "555", "  5", "555"]
six = ["666", "6  ", "666", "6 6", "666"]
seven = ["777", "  7", "  7", "  7", "  7"]
eight = ["888", "8 8", "888", "8 8", "888"]
nine = ["999", "9 9", "999", "  9", "999"]
colon = [" ", ":", " ", ":", " "]
numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

#For each number of the time, set that position to that number
#Then print the output one row at a time
if len(user_input) == 5:
    for i in range(10):
        if user_input[0] == str(i):
            first = numbers[i]
        if user_input[1] == str(i):
            second = numbers[i]
        if user_input[3] == str(i):
            third = numbers[i]
        if user_input[4] == str(i):
            fourth = numbers[i]
    for j in range(5):
        print(first[j], second[j], colon[j], third[j], fourth[j], "")
else: #If it is a time like 1:23, only three positions are filled
    for i in range(10):
        if user_input[0] == str(i):
            first = numbers[i]
        if user_input[2] == str(i):
            third = numbers[i]
        if user_input[3] == str(i):
            fourth = numbers[i]
    for j in range(5):
        print(first[j], colon[j], third[j], fourth[j], "")
