# Weekly Task 8 of 'Programming & Scripting'
# Topics: NumPy and matplotlib
# Author: Mark Gallagher

import numpy as np
import matplotlib.pyplot as plt

# Part 1: Write a histogram of a normal distribuion of a 1000 values, 
# with a mean of 5 and standard deviation of 2

# Step 1: Generate random data
data = np.random.normal(5, 2, 1000) # This will generate a random result

# Step 2: Plot a basic histogram
plt.hist(data, bins=30, color='#008000', edgecolor='#FE5000') 
# This will read the array and produce a histogram

# Step 3: Style the histogram
plt.xlabel ('Chances Created') # Label for x-axis
plt.ylabel ('Minutes') # Label for y-axis
plt.title ('Ireland vs. England (Chances Created)')

# Step 4: Display the plot
plt.show()



# Part 2: Write a plot of the function h(x)=x3 in the range 0 to 10

# Step 1: Generate 100 data points in the range [0,10]
x = np.linspace(0, 10, 100)

# Step 2: Calculate y using x^3
y = x * x * x 

# Step 3: Plot the data
plt.plot(x, y, label='h(x) = x^3', color = "#FF0000") # Plot the function

# Step 4: Add some styling and labels
plt.xlabel('Years in Charge')  # Label for x-axis
plt.ylabel('Total Debt ($ millions)')  # Label for y-axis
plt.title("Glazer Ownership of Manchester United") # The title of the plot
plt.grid(True)  # Display grid
plt.legend() # Display legend

# Step 5: Display the plot
plt.show()