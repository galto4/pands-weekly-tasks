# Weekly Task 2 of 'Programming & Scripting'
# Author: Mark Gallagher

# Step 1: Prompt the user to enter 2 amounts (in cents)

amount_1 = int(input("Please enter the first amount (in cents): "))
amount_2 = int(input("Please enter the second amount (in cents): "))

# Step 2: Add both amounts together

total_amount = amount_1 + amount_2

# Step 3: Print out the answer in a human readable format

euros = total_amount // 100
cents = total_amount % 100

print(f"The total amount is: €{euros}.{cents:02d}")