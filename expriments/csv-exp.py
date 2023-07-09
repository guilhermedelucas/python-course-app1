import csv

with open('../files/weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input('Enter a city: ')
print(data[1:])

for row in data[1:]:
    if row[0] == city:
        exit(row[1])

exit('City does not exists')