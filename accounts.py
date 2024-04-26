# Weekly Task 3 of 'Programming & Scripting'
# Topic: Variables
# Author: Mark Gallagher

# Write a program that reads a 10 character account number, AND
# Outputs the account number with only the last 4 digits showing

# Step 1: Get the 10-digit number from the customer
account_number = input("Please enter your 10-digit account number: ") # input() function

# Step 2: Set-up the masking of the account number
masked_number = "x" * 6 + account_number[-4:] # last 4 numbers displayed

# Step 3: Validate that the Account Number has 10-digits
while len(account_number) != 10: # While Loop
    print("Invalid Account Number! Please enter a valid 10-digit number: ")
    account_number = input("Please enter your 10-digit account number: ")
else: # Python Conditions
    print(masked_number)