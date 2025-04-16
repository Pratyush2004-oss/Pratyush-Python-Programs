str=input("\n Enter a String : ")
count = 0
dict = {}
for i in str:
    count += 1
    dict[i] = str.count(i)
# counting the number of characters in the string
print(f"\n number of characters in the given string is : {count}\n")

# printing the Dictionary
print(dict)

