# Writing modules in python
import math
print(math.pi)

# importing modules
from math import pi
print(pi)

# import objects from modules
from math import pi as p
print(p)

# import all objects from modules
from math import *
print(pi)

# Python built-in modules
import sys
print(sys.path)

# Python built-in modules
import os
print(os.getcwd())

# Python built-in modules
import random
print(random.randint(1, 10))

# Python built-in modules
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))   

# python built-in modules
import platform
print(platform.system())

# python built-in modules
import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data)
print(json_data)

# python built-in modules
# import requests
# response = requests.get("https://api.example.com/data")
# print(response.json())

# python built-in modules
import csv
with open("Student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)