# 01 
# Sum of even numbers
# create a python function that takes a list of integers and returns the sum of all the even numbers in the list



def integralList():
    L1 = []
    n = int(input("Enter the amount of elements in a list: "))
    for i in range(n):
        x = int(input(f"Enter the {i+1}: "))
        L1.append(x)
    return L1

def sumOfEven(L1):
    total = 0
    for x in L1:
        if x%2 == 0:
            total = total + x
    return total

mylist = integralList()
print(sumOfEven(mylist))