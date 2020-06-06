import csv
import math
import datetime
 # Get Current Date

people = []


# import csv file and append data to array
with open('User Locations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x = [row[1], row[2]]
            people.append(x)
            line_count += 1
    print(f'Processed {line_count-1} locations.')
print(people)
# calculate associated infections for each death
distance = []
i = 0
y = 1
while i < len(people):
    Lat1 = float(people[i][0])
    Long1 = float(people[i][1])
    y=1
    while (y + i) < len(people):
        Lat2 = float(people[i+y][0])
        Long2 = float(people[i+y][1])
        a = math.acos(math.cos(math.radians(90 - Lat1)) * math.cos(math.radians(90 - Lat2)) + math.sin(math.radians(90 - Lat1)) * math.sin(math.radians(90 - Lat2)) * math.cos((Long1 - Long2))) * 6371
        if a < 0.002:
            b = datetime.datetime.now()
            print("Person "+str(i)+" and person "+str(y+i)+" are too close "+"@"+str(b.strftime("%Y-%m-%d %H:%M:%S")))
        y+=1
    i += 1
