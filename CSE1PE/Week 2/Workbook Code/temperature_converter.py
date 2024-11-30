# Temperature conversion formulas 
# Fahrenheit - F = 9C/5 + 32
# Celcius - C = (F - 32) x 5/9 = C

conversion = input("Enter the type of temperature you'd like to convert from (Fahrenheit/Celcius): ")
starting_temp = float(input("Enter the temperature you'd like to convert: "))

if conversion == "Fahrenheit":
    converted_temp = (starting_temp - 32) * 5/9
    converted_metric = "Celcius"
elif conversion == "Celcius":
    converted_temp = (9*starting_temp)/5 + 32
    converted_metric = "Fahrenheit"

print("You have converted", starting_temp, conversion, "to", converted_temp, converted_metric)
