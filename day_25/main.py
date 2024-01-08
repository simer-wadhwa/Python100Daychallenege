# with open("weather_data.csv", mode='r') as file:
#     data = file.readlines()
#
# import csv
#
# with open("weather_data.csv", mode='r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     temp =[]
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)
avg = sum(temp_list)/len(temp_list)
print(avg)

print(data["temp"].mean())

print(data["temp"].max())
print(data[data.temp == data.temp.max()])


