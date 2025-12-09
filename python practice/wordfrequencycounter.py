# lis = ["apple", "banana", "apple", "pear", "banana", "apple"]

# freq = {}

# for item in lis:
#     freq[item] = freq.get(item, 0) + 1

# print(freq)

def freqcount(lis):
    freq = {}
    for items in lis:
        freq[items] = freq.get(items, 0) +1
    return freq
    
lis=["apple", "banana", "apple", "pear", "banana", "apple"]
result = freqcount(lis)
print(result)