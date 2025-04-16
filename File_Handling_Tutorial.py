# creating a file
f = open("test.txt", "w")
f.write("Welcome to Python Programming")
f.close()

# reading a file
f = open("test.txt", "r")
print(f.read())
f.close()

# appending a file
f = open("test.txt", "a")
f.write("\nHello World")
f.close()

# deleting a file
import os
os.remove("test.txt")

# checking if a file exists
import os
if os.path.exists("test.txt"):
    print("File exists")
else:
    print("File does not exist")
    

# renaming a file
import os
os.rename("test.txt", "test1.txt")

# copying a file
import shutil
shutil.copy("test1.txt", "test2.txt")

# moving a file
import shutil
shutil.move("test2.txt", "test3.txt")

# creating a directory
import os
os.mkdir("test4")

# removing a directory
import os
os.rmdir("test4")

# listing files in a directory
import os
files = os.listdir()
print(files)

# getting the current working directory
import os
cwd = os.getcwd()
print(cwd)

# changing the current working directory
import os
os.chdir("path/to/directory")

# getting the size of a file
import os
size = os.path.getsize("test1.txt")
print(size)

# getting the creation time of a file
import os
ctime = os.path.getctime("test1.txt")
print(ctime)

# getting the modification time of a file
import os
mtime = os.path.getmtime("test1.txt")
print(mtime)

# getting the access time of a file
import os
atime = os.path.getatime("test1.txt")
print(atime)

# getting the path of a file
import os
path = os.path.abspath("test1.txt")
print(path)

# getting the extension of a file
import os
ext = os.path.splitext("test1.txt")
print(ext)

# getting the base name of a file
import os
base = os.path.basename("test1.txt")
print(base)

# getting the directory name of a file
import os
dir = os.path.dirname("test1.txt")
print(dir)

# getting the size of a directory
import os
size = os.path.getsize("test1.txt")
print(size)

# getting the creation time of a directory
import os
ctime = os.path.getctime("test1.txt")
print(ctime)

# getting the modification time of a directory
import os
mtime = os.path.getmtime("test1.txt")
print(mtime)    
