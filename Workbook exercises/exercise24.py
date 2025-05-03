# Inspired by an exercise from *The Python Workbook* by Ben Stephenson.
#Units of time 1
# create a prg that reads a duration from the user as a number of 
#days hours minutes and seconds and display the total seconds

U_days = int(input("Enter the number of days: "))
U_hours = int(input("Enter the number of hours: "))
U_minutes = int(input("Enter the number of minutes: "))
U_seconds = int(input("Enter the number of seconds: "))

days = 24*60*60 * U_days
hours = 60*60* U_hours
minutes = 60 * U_minutes

Total = days + hours + minutes + U_seconds

print(f"The total number of seconds is {Total}")
