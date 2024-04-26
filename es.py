# Weekly Task 7 of 'Programming & Scripting'
# Module: Programming and Scripting
# Author: Mark Gallagher

# Step 1: Write a program that reads in a text file 
f = open ('mobydick.txt', 'r') # Open the file for reading using the open()function
moby = f.read () # Read the file and create an attribute
f.close () # close() function to free up memory

# Step 2: Output the number of e's that it contains
freq = moby.count ('e') # count() method and create an attribute
print (freq)