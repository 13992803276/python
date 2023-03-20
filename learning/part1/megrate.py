import csv
import datetime

json_objects = []

start_time = datetime.datetime.now()
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        json_objects.append(row)
print(json_objects[0])
print(json_objects[1])
print("read csv success", start_time)
end_time = datetime.datetime.now()
print(end_time - start_time)
