import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import os

root = "./data"
files = sorted(os.listdir(root))
data = []

# Put the scores from each day into data
for file in files:
    filepath = root + "/" + file
    day = []
    for number in open(filepath):
        day.append(int(number.rstrip()))
    data.append(day)

# Create a notched box plot with vertical orientation
plt.boxplot(data, labels=files, notch=True, vert=True)

# Add a title and axis labels
plt.title('Zetamac Progress')
plt.xlabel('Day')
plt.ylabel('Scores')

# Show the plot
plt.show()