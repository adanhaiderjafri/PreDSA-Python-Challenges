d = {
    "fruit": ["apple", "banana"],
    "snack": ["chips", "banana"],
    "drink": ["juice"]
}


rev_dict = {}
for key,values in d.items():
    for items in values:
        print(items)
        if items  in rev_dict:
            rev_dict[items].append(key)
            
        else:
            rev_dict[items] = [key]
print(rev_dict)
            

