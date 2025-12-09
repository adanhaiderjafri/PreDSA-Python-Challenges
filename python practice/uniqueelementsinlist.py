# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# # Expected: ["apple", "banana", "cherry"]
# lis = []
# for items in fruits:
#     if items not in lis:
#         lis.append(items)
# print(lis)
  
def unique(fruits):
    lis = []
    for items in fruits:
        if items not in lis:
            lis.append(items)
    return lis

fruits = ["apple", "banana", "apple", "cherry", "banana"]
result = unique(fruits)
print(result)
