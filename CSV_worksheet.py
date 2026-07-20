import csv

with open("Book2.csv", newline="") as book:
    rows = csv.reader(book)
    temperatures = []

    for row in rows:
        if len(row) >= 3 and row[2] != "Temprature":
            temperatures.append(row[2])

    print(temperatures)