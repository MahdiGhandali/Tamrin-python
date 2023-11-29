from typing import TextIO

f: TextIO = open("demofilee.txt", "r")
a = 0
for x in f:
    a += 1

data = f.read()
words = data.split()

count = len(words)
wordcount = {}

for word in words:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
