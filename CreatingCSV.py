import csv
fh = open("Student.csv","w")

stu = csv.writer(fh)
stu.writerow(["Name" , "Roll Number", "Marks"])
for i in range(5):
    name = input("Enter the Name : " )
    roll = int(input("Enter the Roll number : " ))
    marks = int(input("Enter the marks : " ))
    sturec = [name,roll,marks]
    stu.writerow(sturec)




fh.close()