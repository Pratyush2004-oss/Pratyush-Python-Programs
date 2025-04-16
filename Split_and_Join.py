Str = input("Enter a long String : ")
list = Str.split() #using split function
print("List after splitting the String : ",end='\t')
print(list)

my_string = "--".join(list)#joining the string
#printing the joined string
print("string after joining : ",end='\t')
print(my_string)


