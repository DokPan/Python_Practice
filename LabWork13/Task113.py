import json

fruits = { "apple" : 100, "banana" : 80, "orange" : 120 }

with open("fruits.json", "w") as file:
    json.dump(fruits, file)