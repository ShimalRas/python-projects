# Inspired by an exercise from *The Python Workbook* by Ben Stephenson.
#distance between two points on earth
ufeet = int(input("Enter the amount of feet: "))
uinch = int(input("Enter the inches: "))

inch_to_centi = 2.54 * uinch
foot = 12*ufeet 
centi= foot 
print(f"the amount of centimeters per feet and inches is {ufeet * foot + inch_to_centi}")