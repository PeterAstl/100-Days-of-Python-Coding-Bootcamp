#
# with open("./weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
#
# #
# # temp_list = data["temp"].to_list()
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp[0])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(Cinnamon_squirrels)
print(black_squirrels)

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black",],
    "Count": [gray_squirrels, Cinnamon_squirrels, black_squirrels],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels.csv")