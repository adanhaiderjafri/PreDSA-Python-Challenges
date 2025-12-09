students = [
  ("A", "Ali"),
  ("B", "Sara"),
  ("A", "Khan"),
  ("C", "John"),
  ("B", "Tara")
]
dic  = {}
for key,value in students:
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = [value]
print(dic)
   
