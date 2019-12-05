word = input("Type a word: ")
step = int(input("Type step: "))
encoded_word = []

for el in word:
    next_letter = chr(ord(el) + step)
    encoded_word.append(next_letter)

encoded_word = "".join(encoded_word)
print(encoded_word)