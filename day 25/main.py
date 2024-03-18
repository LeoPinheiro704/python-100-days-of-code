# import csv

# with open("./weather_data.csv") as weather_file:
#   data = csv.reader(weather_file)
#   temperatures = []
#   for row in data:
#     if row[1] != 'temp':
#       temperatures.append(int(row[1]))
#   print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns 
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Create a dataframe from scratch
# data_dict = {
#   "students": ["Amy", "James"],
#   "scores": [76, 56]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240318.csv")
squirrel_colors = ["Gray", "Cinnamon", "Black"]
squirrel_colors_data = {
  "Fur Color": [],
  "Count": []
}
for color in squirrel_colors:
  count = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
  squirrel_colors_data["Fur Color"].append(color)
  squirrel_colors_data["Count"].append(count)
data = pandas.DataFrame(squirrel_colors_data)
data.to_csv("squirrel_data.csv")

