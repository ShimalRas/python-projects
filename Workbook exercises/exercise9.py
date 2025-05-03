# Inspired by an exercise from *The Python Workbook* by Ben Stephenson.
#Compound interest 
#you have a savings acc that earns a fixed interest per year and is added to the balance savings.
#the program should read the amount deposited and compute  and display the amount in thr account after a fixed amount of years.

fixed_interest_rate = 5/100

amount_deposited = float(input("Enter the amount of money in savings account: "))

fixed_years = int(input("Enter the amount of years to compute: "))
year = 0
interest = amount_deposited
while year< fixed_years:
    year = year+1
    interest = interest * fixed_interest_rate + interest
    print(f"in {year} years the account will have {round(interest,2)} amount of money")
    