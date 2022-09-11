import csv
f = open("student.csv", "w")
a = csv.writer(f)
b = [['Amit', 45], ['Anand', 17]]
a.writerows(b)
f.close()
