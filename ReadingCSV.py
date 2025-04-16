import csv

fh = open("Student.csv")

stu = csv.reader(fh)

for row in stu:
    print(row)

fh.close()
