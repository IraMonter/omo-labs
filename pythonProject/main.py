import numpy as np
import csv

with open("./friends_episodes_v2.csv") as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        print(row)