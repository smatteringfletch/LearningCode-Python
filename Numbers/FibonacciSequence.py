# The starting two numbers and our temporary field are configured
n1 = 0
n2 = 1
temp = 0
# Ask the user how many digits of the fibonacci sequence they'd like to print
iterations = int(input("How many iterations of the fibonacci sequence would you like to print?: "))

# The for loop adds the last two numbers together and prints out the scale up til the digit in the input above
for x in range(iterations):
    print(str(n1), end=", ")
    temp = n1 + n2
    n2 = n1
    n1 = temp