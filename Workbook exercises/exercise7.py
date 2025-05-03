# Inspired by an exercise from *The Python Workbook* by Ben Stephenson.

#Sum of the first n positive integers
#program reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
#the sum of the first n positive integers can be computed using the formula: sum = (n)(n+1)/2
user_input = int(input("Enter a postive number: "))

while (user_input <0)== True:
    user_input = int(input("Enter a postive number: "))


sum = (user_input )*(user_input + 1)/2
print(f"the sum of the first {user_input} integers is {sum}")