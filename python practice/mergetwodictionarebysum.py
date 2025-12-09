d1 = {"apple": 3, "banana": 5}
d2 = {"banana": 4, "orange": 2}
dic = {}

for k,v in d1.items():
    dic[k] = v

for k ,  v in d2.items():
    dic[k] = dic.get(k,0) + v
print(dic)