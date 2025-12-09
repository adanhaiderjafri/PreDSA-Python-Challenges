records = [
  ("Alice", "fruit"),
  ("Bob", "drink"),
  ("Alice", "snack"),
  ("Bob", "fruit"),
  ("Alice", "fruit")
]

dic = {}
for k,v in records:
    if k not in dic:
        dic[k] = {}
    dic[k][v] = dic[k].get(v,0)+1
print(dic)
