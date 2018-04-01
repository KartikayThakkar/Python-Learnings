# csv - Comma seperated values

import csv

data = [
    "Name,Score,Average".split(","),
    "Sachin,67,54".split(","),
    "Virat,78,52".split(","),
    "Dhoni,50,55".split(","),
    "Yuvraj,89,49".split(",")
]

with open('scores.csv','w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for d in data:
        writer.writerow(d)

