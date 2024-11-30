total_pizza_slices = int(input("How many pizza slices do you have: "))
total_guest = int(input("How many total guest are there: "))

slices_per_guest = total_pizza_slices // total_guest

print(str(slices_per_guest) , "per person")