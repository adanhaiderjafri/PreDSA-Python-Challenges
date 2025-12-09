
scores = [
  ("Ali", 84),
  ("Sara", 91),
  ("Ali", 90),
  ("Sara", 85),
  ("Ali", 95)
]

dic = {}

for name, score in scores:
    if name not in dic:          
        dic[name] = score

    else:
        if score > dic[name]:    
            dic[name] = score

print(dic)

