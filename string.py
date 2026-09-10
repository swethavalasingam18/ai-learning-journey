string ="the cat sat on the mat the cat ran"
words = string.split(' ')

word_count = {}   # empty dictionary to start

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1   # already seen it, add 1
    else:
        word_count[word] = 1                       # first time seeing it, start at 1

print(word_count)