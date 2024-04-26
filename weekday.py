# Weekly Task 5 of 'Programming & Scripting'
# Topic: Lists, Tuples and Dictionary
# Author: Mark Gallagher

# Write a program that outputs whether or not today is a weekday

import datetime # Allows us to work with dates and times in their Python programs

# Step 1: Let's discover today's date
today = datetime.datetime.today()

# Step 2: Let's check whether today is a weekday or weekend
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday. Keep working!")
else:
    print("It is the weekend, Yay! Turn off your computer!")