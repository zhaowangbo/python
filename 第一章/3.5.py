s = "hello albert albert say hello world world"

# 1
words = s.split(" ")
word_dict = {}
for word in words:
    if word not in word_dict:
        word_dict.update({word: 1})
    else:
        word_dict[word] += 1
print(word_dict)

# 2

words = s.split(" ")
a = dict((i, words.count(i)) for i in words)
print(a)