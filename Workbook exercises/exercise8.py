#widgets and gizmos
#basically the program is to calculate and display the total weight of two objects in different quantities and display the total

widgets_qty = int(input("Enter the amount of widgets: "))
gizmos_qty = int(input("Enter the amount of gizmos: "))
widgets = 75
gizmos = 112
total_weight = widgets_qty*widgets + gizmos_qty*gizmos

print(f"The total weight of the order is {total_weight} grams")