import csv
f = open("student.csv", "r", newline='\r\n')
a = csv.reader(f)
for rec in a:
    print(rec)
