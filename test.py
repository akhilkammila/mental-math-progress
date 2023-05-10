import numpy as np
import matplotlib.pyplot as plt

# Create some sample data for 3 days
day1_data = np.random.normal(loc=10, scale=2, size=100)
day2_data = np.random.normal(loc=8, scale=1.5, size=100)
day3_data = np.random.normal(loc=12, scale=3, size=100)

# Create a list of data for each day
data = [day1_data, day2_data, day3_data]

# Set the positions and labels for the x-axis
positions = [1, 2, 3]
labels = ['Day 1', 'Day 2', 'Day 3']

# Create a notched box plot with vertical orientation
plt.boxplot(data, positions=positions, labels=labels, notch=True, vert=True)

# Add a title and axis labels
plt.title('Notched Box Plots by Day')
plt.xlabel('Day')
plt.ylabel('Value')

# Show the plot
plt.show()