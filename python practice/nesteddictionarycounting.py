records = [
    ("Alice", "fruit"),
    ("Bob", "drink"),
    ("Alice", "fruit"),
    ("Alice", "snack"),
    ("Bob", "fruit")
]

# Initialize empty dictionary
result = {}

for name, item in records:
    # If the name is not yet in result, add it with an empty dictionary
    if name not in result:
        result[name] = {}
    # Count the item for this name
    if item in result[name]:
        result[name][item] += 1
    else:
        result[name][item] = 1

print(result)



        
     

   
