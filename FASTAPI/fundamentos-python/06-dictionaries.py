user = {
    "name": "eliana",
    "age": 21,
    "email": "valdezeliana38@gmail.com",
    "active": True,
    (19.12, -98.32): "Cancún mexico",
}

user["name"] = "Eliana"
user["age"] = 22
print(user[(19.12, -98.32)])
user["country"] = "Argentina"
# values, items, keys

print(user.items())
print(user.values())
print(user.keys())
