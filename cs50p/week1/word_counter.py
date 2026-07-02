text=input("Text: ")
text=text.lower()
words=text.split()

word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

for word,count in sorted_words[:10]:
    print(word,count)