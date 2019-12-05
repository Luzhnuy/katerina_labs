sentence = input("Write your sentence: ")

sentence = sentence.split()
counter = 0
for word in sentence:
    if len(word) > 2 and word != "," and word != ".":
        counter+=1

print(counter)