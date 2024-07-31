import csv
fh = open("Student.csv","w",newline='')

stu = csv.writer(fh)
stu.writerow(["Name" , "Roll Number", "Marks"])
stulist = []

for i in range(5):
    name = input("Enter the Name : " )
    roll = int(input("Enter the Roll number : " ))
    marks = int(input("Enter the marks : " ))
    stulist.append([name,roll,marks])

stu.writerows(stulist)
fh.close()