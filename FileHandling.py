fileout = open("testFile.txt","w")
for i in range(3):
    name = input("Enter Name : ")
    roll = input("Enter Roll Number : ")
    marks = input("Enter marks : ")
    fileout.writelines("name : " + name + "\t" + "Roll Number : " + roll + "\t" + "Marks : " + marks + "\n")

fileout.close()
