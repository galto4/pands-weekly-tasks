# Weekly Task 6 of 'Programming & Scripting'
# Topic: Functions and Modules
# Author: Mark Gallagher

import math # This imports the math module

# Step 1: Ask the user to input a positive integer
positive_number = float(input("Plese enter a positive number: "))

# Step 2: Calculate the square root using Newton's Methond
approx = 0.5 * positive_number # Assume approx. as half the inputted number
better = 0.5 * (approx + positive_number / approx) # Find a better value
while (better != approx): # While better found is not equal to the assumed approx.
    approx = better # Assume the found better value as approx.
    better = 0.5 * (approx + positive_number / approx) # Recalculate better value

# Step 3: Print the result
print(f"The square root of {positive_number} is", better)

# Thank goodness I found 'The Last Minute Professor' :)


'''
# Option 2: Using the built-in math.sqrt function

# Step 1: Entering a positive number
positive_number = float(input("Please enter a positive number: "))

# Step 3: Calculating the Square Root
square_root = math.sqrt(positive_number)

# Step 4: Printing the final statement
print(f'The square root of {positive_number} is : {square_root}')
'''