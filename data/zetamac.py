import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import os
from datetime import datetime

game = 'zetamac_overall'

# 1. Retrieve Data
# Sort files first by date, then by alphabetical
def fileComparator(file):
    date_str = " ".join(file.split('_')[:3])
    date_obj = datetime.strptime(date_str, '%b %d %Y')
    return (date_obj, file)

root = "./data/" + game
files = sorted(os.listdir(root), key=fileComparator)
data = []

# Put the scores from file into data
for file in files:
    filepath = root + "/" + file
    day = []
    for number in open(filepath):
        day.append(int(number.rstrip()))
    data.append(day)


# 2. Plot Data
# Create a notched box plot with vertical orientation
plt.boxplot(data, labels=files, notch=True, vert=True)

# Add a title and axis labels
plt.title(game + " scores")
plt.xlabel('Day')
plt.ylabel('Scores')

# Show the plot
plt.show()