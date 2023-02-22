import csv , operator
names = []
with open("artist_names.csv", 'r') as file:
    data = csv.reader(file, delimiter=',')
    names = sorted(data, key=operator.itemgetter(0))[0]


print(names[1])