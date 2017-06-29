# Find the Square Root of a number:

import math



targetNumber = 65



print(math.sqrt(targetNumber))

# Function of which to find the root
def f(x):
    return x * x - targetNumber
# Derivative of f(x)
def fprime(x):
    return 2 * x

x0 = 8 # Initial value to test, try to get as close to the sqrt as possible.

tolerance = math.pow(10, -7) # Accuracy to seven decimal digits
epsilon = math.pow(10, -14) # Don't want to divide by a number smaller than this.

maxIterations = 20
foundSolution = False

i = 1
for i in range(maxIterations):
    y = f(x0)
    yprime = fprime(x0)

    # If yprime is too small, break. Do not divide by zero
    if(abs(yprime) < epsilon):
        print(abs(yprime))
        break

    # Newton's Method
    x1 = x0 - y/yprime

    # If the result is accurate to the correct number of decimal places, break the loop
    if (abs(x1 - x0)) <= tolerance * abs(x1):
        foundSolution = True
        break

    x0 = x1

if (foundSolution):
    print("Solution: ", x0)
else:
    print("No solution found.")

