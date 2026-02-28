#ЗАДАЧА  1
chek = lambda x: "положительное" if x> 0 else ("ноль" if x == 0 else "отрицательное")
print(chek(-5))
print(chek(0))
print(chek(2))

#ЗАДАЧА 2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
words_sorted = sorted(words, key = lambda word: (len(word), word[0]))
print(words_sorted)

#ЗАДАЧА 3
numbers = [5, 12, 7, 20, 33, 8]
numbers_filtered = list(filter(lambda x: x%2 ==0 and x>10 , numbers))
print(numbers_filtered)