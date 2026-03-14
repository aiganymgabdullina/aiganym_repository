#ЗАДАЧА  1
chek = lambda x: "положительное" if x> 0 else "ноль" if x == 0 else "отрицательное"
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

#ЗАДАЧА 6
numbers = [0, -3, 5, -7, 8]
result =  [(lambda x: "положительное" if x>0 else("ноль" if x==0 else "отрицательное"))(x) for x in numbers]
print(result)
print("------------------------------------------------------------------------------")

print("ГЕНЕРАТОРЫ")
#ЗАДАЧА 1
def even_numbers(n):
    for i in range(1, n+1):



        if i%4 ==0:
            yield "кратно 4"
        else:
            yield i

for x in even_numbers(10):
    print(x)

#ЗАДАЧА 2
def filter_words(words):
    for i in words:
        if len(i) > 4:
            if "а" in i:
                yield "c a"
            else:
                yield i

words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)

#ЗАДАЧА 3
def infinite_numbers():
    i = 1
    while True :
        if i%3 == 0 and i%5 ==0:
            yield "FizzBuzz"
        elif i%3 == 0 :
            yield "Fizz"
        elif i%5 ==0:
            yield "Buzz"
        else:
            yield i
        i+=1
a = infinite_numbers()
for x in range(16):
    print(next(a))

#ЗАДАЧА 4
def squares(n):
    for i in range(1, n+1):
        a= i**2
        if a%2 ==0:
            yield "четный квадрат"
        else:
            yield a
for x in squares(5):
    print(x)

print("------------------------------------------------------------------------------")
print("Итераторы и comprehension")
#ЗАДАЧА 1
numbers_squares = [n**2 for n in range(1, 21) if n%2 ==0]
print(numbers_squares)

#ЗАДАЧА 2
matrix = [[1,2,3], [4,5,6], [7,8,9]]
new_matrix = [ (lambda x: 1 if not x else x[0] * x[1] * x[2])(x) for x in matrix ]
print(new_matrix)

#ЗАДАЧА 3
words = ["кот", "машина", "ананас", "дом"]
new_words = [word for word in words if len(word)>4 and "а" not in word]
print(new_words)

#ЗАДАЧА 4
numbers = [1,2,3,4,5]
numbers_dict = {n: "четное" if n%2 == 0 else "нечетное" for n in numbers}
print(numbers_dict)

#ЗАДАЧА 5
matrix = [[1,2], [3,4], [5,6]]
matrix_new = [element for list1 in matrix for element in list1]
print(matrix_new)

#ЗАДАЧА 6
new_list = ["FizzBuzz" if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n for n in range(1, 21)]
print(new_list)

print("------------------------------------------------------------------------------")
print("Смешанные сложные задачи")

#ЗАДАЧА 1
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def special_numbers(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0 :
            yield "FizzBuzz"
        elif i%3==0:
            yield "Fizz"
        elif i%5==0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for x in special_numbers(15):
    print(x)


#ЗАДАЧА 2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
words_2 = [(lambda word: (word.upper() if len(word)>4 else "short" ) +( "*" if "a" in word else ""))(word)for word in words]
print(words_2)

#ЗАДАЧА 3
def process_numbers(numbers):
    gen = (num for num in numbers)
    numbers_filtered = filter(lambda x: x>= 0, gen)
    processed = map(lambda x: x/2 if x%2 ==0 else x*3+1, numbers_filtered)
    return processed
numbers = [5, -2, 8, 0, -7, 3]
for x in process_numbers(numbers):
    print(x)



#ЗАДАЧА 4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
grades = lambda x : ("отлично" if x >= 90 else("хорошо" if x <90 and x >= 70 else "Удовлетворительно"))
students_dict = {name: grades(x) for name, x in students}
print(students_dict)


#ЗАДАЧА 5
def matrix_transform(matrix):
    for n in (num for list1 in matrix for num in list1):
        if n%2 ==0 and n%3 ==0:
            yield "кратно 6"
        elif n%2 ==0:
            yield "чётное"
        elif n%3 ==0 :
            yield "кратно 3"
        else :
            yield n
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)

print("------------------------------------------------------------------------------")
print("Задачи для понимания map and filter")

#ЗАДАЧА 1
numbers = [1, 2, 3, 4, 5]
numbers_map = list(map(lambda n: n*2, numbers ))
print(numbers_map)

#ЗАДАЧА 2
words = ["кот", "машина", "арбуз", "дом"]
words_map = list(map(lambda word: word.upper() + "!" if len(word)>3 else word.upper(), words))
print(words_map)

#ЗАДАЧА 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_new = list(filter(lambda n : n%2 == 0, numbers))
print(numbers_new)

#ЗАДАЧА 4
numbers = [0, 5, 12, 7, 20, -3, 8]
numbers_map = list(map(lambda n: n/2 if n%2==0 else n*3, filter(lambda n: n>5 , numbers)))
print(numbers_map)


