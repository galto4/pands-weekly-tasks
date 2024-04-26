# Weekly Task 2 of 'Programming & Scripting'
# Topic: Statements
# Author: Mark Gallagher

# Step 1: Prompt the user to enter two money amounts and convert to integers
amount1 = int(input("Please enter your first amount: ")) # input() function
amount2 = int(input("Please enter your second amount: "))

# Step 2: Add the two amounts together, AND create a new variable
total_amount = amount1 + amount2  # Creating a variable
total_currency = total_amount / 100

# Step 3: Print the answer in a human readable format (€0.00)
print("The total amount is: €" + "%.2f" % total_currency) # Using the %f formatter


# Sources: https://www.askpython.com/python/built-in-methods/format-2-decimal-places