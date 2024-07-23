fileout = open("testFile.txt","w")
for i in range(5):
    name = input("Enter Name : ")
    fileout.writelines(name + "\n")

fileout.close()
