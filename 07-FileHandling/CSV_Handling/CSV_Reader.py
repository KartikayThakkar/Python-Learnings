import csv
# import pandas as pd

with open('scores.csv') as file:
    reader = csv.reader(file)

    # print(reader)
    # print(list(reader))
    for data in list(reader)[1:]:
        # print(data[0], data[1], data[2])
        if int(data[1]) < 80:
            print(data)

# data = pd.read_csv('scores.csv')
# print(data)