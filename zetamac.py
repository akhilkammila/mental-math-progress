import matplotlib.pyplot as plt
import os

root = "./data"
files = os.listdir(root)

data = []
for file in files:
    filepath = root + "/" + file

    day = []
    for number in open(filepath):
        day.append(int(number.rstrip()))
    data.append(day)
print(data)