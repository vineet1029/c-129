import csv

data1 = []
data2 = []

with open("bright_star.csv") as file :
    reader = csv.reader(file)
    for i in reader:
        data1.append(i)

with open("dwarf_star.csv") as file :
    reader = csv.reader(file)
    for i in reader:
        data2.append(i)

headers1 = data1[0]
starData1 = data1[1:]

headers2 = data2[0]
starData2 = data2[1:]

headers = headers1 + headers2

star_Data = []

for i, data in enumerate(starData1):
    star_Data.append(starData1[i] + starData2[i])

with open("merged.csv", "a+") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(star_Data)