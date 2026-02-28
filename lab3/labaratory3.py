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

#ЗАДАЧА 4
numbers = [1, 2, 3, 4, 5, 6]
numbers_chek = list(map(lambda x: x**2 if x%2 ==0 else x*3, numbers))
print(numbers_chek)

#ЗАДАЧА 5
compare = lambda a, b: "a больше" if a>b else("равны" if a==b else "b больше")
print(compare(10, 7))
print(compare(3, 5))
print(compare(4, 4))