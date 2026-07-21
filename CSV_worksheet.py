# with open("Book2.csv") as book:
#     data = book.read();
#     print(data)
    # output:
    # Area,Wether,Temprature
    # Kotturu,Cloudy,29
    # Ln peta ,Sunny,41
    # Hiramandalam ,Sunny,38

import csv


# with open("Book2.csv") as book:
#     data = csv.reader(book)
#     for row in data:
#         print(row[2])         # output:-['29', '41', '38']


# with open("Book2.csv") as book:
#     temprature = []
#     data = csv.reader(book)
#     for row in data:
#         if row[2]!="Temprature":
#             temprature.append(row[2])
#     print(temprature)           # output:-['29', '41', '38']
import pandas

data = pandas.read_csv("Book2.csv")
# print(data[Temprature])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["Temprature"].to_list()
# temp_village = data["Area"].to_list()
# temp_wether = data["Wether"].to_list()
# print(temp_list)    #[29, 41, 38]
# print(temp_village) #['Kotturu', 'Ln peta ', 'Hiramandalam ']
# print(temp_wether)  #['Cloudy', 'Sunny', 'Sunny']

# print(data["Temprature"].mean()) 
# # output : 36.0
# print(data["Temprature"].max())
# # output : 41
# print(data["Temprature"].min())
# # output : 29

#get data in columns

# print(data[data["Wether"]=="Sunny"])
#output for the above line
#             Area Wether  Temprature
# 1       Ln peta   Sunny          41
# 2  Hiramandalam   Sunny          38

print(data[data["Temprature"]==data["Temprature"].max()])