d1 = {"apple": 3, "banana": 4}
d2 = {"apple": 2, "orange": 5}

for key, value in d2.items():
    d1[key] = d1.get(key, 0) + value

print(d1)


