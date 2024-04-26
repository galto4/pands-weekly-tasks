# Weekly Task 4 of 'Programming & Scripting'
# Topic: Conditions and If Statements
# Author: Mark Gallagher

# Step 1: Ask the user to input any positive integer
number = int(input("Please input a positive integer: ")) # input() function and variable created

# Step 2: Check to validate that the user has not entered zero
while number <= 0: # While Loop to check if number is equal to or less than 0
    print ("Please enter a number greater than 0! ") 
    number = int (input ("Hey! I asked for a positive integer: "))

print (number) # prints the number selected

# Step 3: If the number is 1: End the program

while number != 1:  # this will end the program as there's no other commands

# Step 4: If the number is Odd: Multiply by 3, and Add 1     
    if number % 2 == 0: # this is an even number
        print (number // 2)  # this will print the number divided by 2 
        number = number // 2  # number is now number divided by 2 

# Step 5: If the number is Even: Divide by 2
    elif number % 2 == 1:  # odd number
        print (number * 3  + 1)  # print number * 3 + 1 
        number = number * 3 + 1  # number is now number multiplied by 3 + 1 