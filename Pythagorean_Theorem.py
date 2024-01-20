
# Taking input from user for the following points

x1 = int(input("Enter the x-coordinates of first point : "))
y1 = int(input("Enter the y-coordinates of first point : "))
# printing first point 
print(f"Point A : { (x1,y1) }")

x2 = int(input("Enter the x-coordinates of second point : "))
y2 = int(input("Enter the y-coordinates of second point : "))
# printing second point
print(f"Point B : { (x2,y2) }")

distance = pow(pow((x1-x2),2) + pow((y1-y2),2),1/2)
# printing the distance between the 2 points
print(f"Distance between 2 points A{ (x1,y1) } and B{ (x2,y2) } is : {distance} units")



