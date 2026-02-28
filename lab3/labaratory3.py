#ЗАДАЧА  1
chek = lambda x: "положительное" if x> 0 else ("ноль" if x == 0 else "отрицательное")
print(chek(-5))
print(chek(0))
print(chek(2))

#ЗАДАЧА 2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
words_sorted = sorted(words, key = lambda word: (len(word), word[0]))
print(words_sorted)

