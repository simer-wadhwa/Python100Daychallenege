import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240108.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(gray.count())
print(grey_squirrels_count)

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [black_squirrels_count, cinnamon_squirrels_count,grey_squirrels_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")