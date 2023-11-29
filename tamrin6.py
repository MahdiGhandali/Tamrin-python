def word_count(sentence):
    words = sentence.split()

    total_words = len(worsds)

    word_countt = {}

    for word in words:
        if word in word_countt:
            word_countt{word} +=1
        else:
        word_countt{word}=1

    longest_word = max(words,key=len)

    print(f"Total number of words: {total_words}")
    print("word counts:")
    for word, count in word_countt.items():
        print(f"(word): {count}")
    print(f"Length of the longest word: {len(longest_word)}")

input_sentence = input("enter a sentence")
word_count(input_sentence)

for item in input_sentence:
    if item in "aiceuo":
        input_sentence = input_sentence.replace(item,"a")
print(input_sentence)
