# sentence = input("tell me sentence :")
# words = sentence.split()

# max_len = 0
# max_word = ""
# for w in words:
    
#     if len(w) > max_len:
#         max_len = len(w)
#         max_word = w
# print("word with maximum length is :", max_word)

def maxfreq(sentence):
    words = sentence.split()
    max_len = 0
    max_word  = ""
    for w in words:
        if len(w) > max_len:
            max_len = len(words)
            max_word = w
            return f"Word With Max Lenght is: {max_word}"
print(maxfreq("Hello my name is adan"))

