import os
from datetime import datetime

root = "./data"
files = sorted(os.listdir(root))
data = []

for file in files:
    date_str = " ".join(file.split('_')[:3])
    date_obj = datetime.strptime(date_str, '%b %d %Y')
    print(date_obj)