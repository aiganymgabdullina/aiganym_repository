#1 esep
from operator import truediv


def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for alpha in text1:
        if alpha.isalpha() or alpha == " ":
            text2 += alpha
    dauysty = "aeiouy"
    zhana_text = ""
    for alpha in text2:
        if alpha in dauysty:
            zhana_text += alpha
    text3 = text2.split()
    jauap = ""
    text4 = ''
    for word in text3:
        if len(word) >= 5:
            if word[0] == word[-1]:
                if word not in jauap:
                    jauap += word + " "
                    text4 += word + "," + " "

    return {
        "дауысты әріптер:" : set(zhana_text),
    "дауысты әріптер саны:": len(set(zhana_text)),
        "слова длиной ≥ 5:": text4,
        "жауабы:":jauap
    }
kerek_matyn = input("1 esep : мәтін:")
print(analyze_text(kerek_matyn))



#2 esep
process = lambda s: " ".join(words := list(filter(
    lambda word: len(word) % 2 == 0,
    reversed_w := list(map(
        lambda word: word[::-1],
        no_digits := list(filter(
            lambda word: all(not ch.isdigit() for ch in word),
            s.split()
        ))
    ))
)))

text = input("2 esep: мәтін: ")
print(process(text))

#3 esep
def top_k_words(text, k):
    import string
    text = text.lower()
    clean_text = ""
    for ch in text:
        if ch not in string.punctuation:
            clean_text += ch
    words = clean_text.split()
    f = {}
    for word in words:
        if word in f:
            f[word] += 1
        else:
            f[word] = 1
    f_list = []
    for word in f:
        f_list.append((word, f[word]))
    for i in range(len(f_list)):
        for j in range(i + 1, len(f_list)):
            if f_list[j][1] > f_list[i][1]:
                f_list[i], f_list[j] = f_list[j], f_list[i]
            elif f_list[j][1] == f_list[i][1]:
                if f_list[j][0] < f_list[i][0]:
                    f_list[i], f_list[j] = f_list[j], f_list[i]
    top_words = []
    for i in range(min(k, len(f_list))):
        top_words.append(f_list[i][0])

    return top_words
text = "Hello world! Hello Python. Python, python, code."
print("3 esep", top_k_words(text, 2))

#4 esep
process = lambda s: " ".join(
    lower_w:= list(
        map(
            lambda w: w.lower(),
            filtered_w := list(
                filter(
                    lambda w: sum(1 for ch in w if ch.isupper()) == 1
                              and not w[0].isupper()
                              and not w[-1].isupper(),
                    s.split())))))
text = input("4 esep: мәтін: ")
print(process(text))

#5 esep
def compress_text(text):
    if not text:
        return ""

    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i - 1].lower():
            count += 1
        else:
            if count > 1:
                result += text[i - 1] + str(count)
            else:
                result += text[i - 1]
            count = 1
    if count > 1:
        result += text[-1] + str(count)
    else:
        result += text[-1]
    return result
print("5 esep: ", end="")
print(compress_text("AaaBBBcc"))

#6 esep
filter_words = lambda s: list(
    filter(
        lambda w: len(w) >= 4
        and w.isalpha()
        and len(set(w.lower())) == len(w),
        s.split()
    )
)
text = "apple moon pencil  school sun sky"
print("6 esep: ", filter_words(text))

#7 esep
def palindrome_words(text):
    proverka = ""
    for ch in text:
        if ch.isalpha() or ch.isspace():
            proverka += ch.lower()
    words = proverka.split()
    unique_palindromes = []
    for word in words:
        if len(word) >= 3 and word == word[::-1]:
            if word not in unique_palindromes:
                unique_palindromes.append(word)
    unique_palindromes.sort(key=lambda w: (-len(w), w))
    return unique_palindromes
text = "Madam, level, noon, gagag! radar level kayak?"
print("7 esep: ", palindrome_words(text))

#8 esep
text = "Apple banana 123start orange Car7 dog"

result = (lambda s: " ".join(
    map(lambda word: word if any(ch.isdigit() for ch in word)
        else "VOWEL" if word[0].lower() in "aeiou"
        else "CONSONANT",
        s.split())
))(text)
print("8 esep: ",result)

#9 esep
def alternate_case_blocks(text, n):
    result = ""
    block_number = 0
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if block_number % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()
        block_number += 1
    return result.replace(" ", "")
print("9 esep: ", alternate_case_blocks("HelloWorldPython", 5))

#10 esep
count_words = lambda s: sum(
    1 for word in s.split()
    if any(ch.isdigit() for ch in word)
    and not word[0].isdigit()
    and len(word) >= 5)
text = "hello abc12 1test test1234  good1 day"
print("10 esep: ",count_words(text))

#11 esep
def common_unique_chars(s1, s2):
    result = ""
    for ch in s1:
        if ch == " " or ch.isdigit():
            continue
        if ch in s2 and ch not in result:
            if ch != " " and not ch.isdigit():
                result += ch
    return result
print("11 esep: ", common_unique_chars("hello world 123", "yellow bird"))

#12 esep
filter_words = lambda s: list(
    filter(lambda w: len(w) > 3
                     and w[0].lower() == w[-1].lower()
                     and w.lower() != w.lower()[::-1],
           s.split()))
print("12 esep: ", filter_words("apple moon pencil  school sun sky test alpha"))

#13 esep
def replace_every_nth(text, n, char):
    result = ""
    words = text.split(" ")
    index = 0
    for word in words:
        newword = ""
        for ch in word:
            if (index + 1) % n == 0 and not ch.isdigit() and len(word) >= 3:
                newword += char
            else:
                newword += ch
            index += 1
        result += newword + " "
        index += 1
    return result.rstrip()
print("13 esep: ", replace_every_nth("hello to you 123 world", 2, "*"))

#14 esep
func = lambda s: ",".join(
    filter(
        lambda w: len(set([c.lower() for c in w if c.isalpha()])) > 3
        and all(w.lower().count(v) <= 1 for v in "aeiou"),
        s.split()))
print("14 esep: ", func("planet moon apple sky sleep book train"))

#15 esep
def word_pattern_sort(text):
    vowels = "aeiouаеёиоуыэюя"
    words = text.split()
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    result = []
    for length in sorted(groups.keys()):
        group = groups[length]
        for i in range(len(group)):
            for j in range(len(group) - 1):
                v1 = sum(1 for c in group[j].lower() if c in vowels)
                v2 = sum(1 for c in group[j + 1].lower() if c in vowels)
                if v1 < v2 or (v1 == v2 and group[j] > group[j + 1]):
                    group[j], group[j + 1] = group[j + 1], group[j]
        result.extend(group)
    return result
print("15 esep: ", word_pattern_sort("apple dog cat area sky orange book"))

#16 esep
def transform_list(nums):
    result = []
    for num in nums:
        if num < 0:
            continue
        if num % 2 == 0:
            result.append(num ** 2)
        elif num > 10:
            digit_sum = 0
            for d in str(num):
                digit_sum += int(d)
            result.append(digit_sum)
        else:
            result.append(num)
    return result
print("16 esep: ", transform_list([4, -3, 15, 7, 12, 9, 23]))

#17 esep
func = lambda nums: list(
    map(lambda x: x**2,
        filter(lambda x: (x % 3 == 0 or x % 5 == 0)
                         and x % 15 != 0
                         and len(str(abs(x))) % 2 == 1,
               nums)))
print("17 esep: ", func([3,5,15,30,105,7,111]))

#18 esep
def flatten_and_filter(lst):
    flat = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in current:
                stack.append(item)
        else:
            if isinstance(current, int):
                flat.append(current)
    result = []
    for num in flat:
        if num > 0 and num % 4 != 0 and len(str(abs(num))) > 1:
            result.append(num)
    result.sort()
    return result
print("18 esep: ", flatten_and_filter([1, [12, -5, [33, 8]],[44,[21,[7,105]]]]))

#19 esep
func = lambda a, b: list(
    filter(lambda x: x % 2 == 0,
           [x for x, y in zip(a, b) if x == y]))
print("19 esep: ", func([2, 3, 4, 6], [2, 5, 4, 7]))

#20 esep
def max_subarray_sum(nums, k):
    max_sum = None
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        if all(num> 0 for num in window):
            s = sum(window)
            if max_sum is None or s > max_sum:
                max_sum = s
    return max_sum
print("20 esep: ", max_subarray_sum([1,2,3,-1,4,5],2))

#21 esep
task21 = lambda lst: [
    s.upper()
    for s in lst
    if s.isalpha() and len(s) > 4 and len(set(s)) == len(s)]
print("21 esep: ",task21(["Hello", "World", "Python", "abcde", "Letter", "Code1"]))

#22 esep
def group_by_parity_and_sort(nums):
    jup = []
    taq = []
    for num in nums:
        if num % 2 == 0:
            jup.append(num)
        else:
            taq.append(num)
    jup.sort()
    taq.sort()
    return jup + taq
print("22 esep: ", group_by_parity_and_sort([5, 2, 8, 1, 4, 7]))


#23 esep
result = lambda lst: list(
    filter(
        lambda x: x % 2 != 0 and x > sum(lst)/len(lst),
        [lst[i] for i in range(len(lst)) 
         if i > 1 and all(i % d != 0 for d in range(2, int(i**0.5) + 1))] ))
print("23 esep: ",result([3,7,2,9,5,8,11,4,13]) )


#24 esep
def longest_increasing_sublist(nums):
    if not nums:
        return []
    longest = []
    current = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]
    if len(current) > len(longest):
        longest = current
    return longest
print("24 esep: ", longest_increasing_sublist([1,2,2,3,4,1,2,3,4,5]))

#25 esep
result = lambda lst: list(
    map(lambda x: sum(x) / len(x),
        filter(lambda x: len(x) >= 3 and sum(x) % 2 == 0, lst)))
print("25 esep: ", result([[1,2,3], [2,4,6],[1,1],[5,5,2]]))

#26 esep
def remove_duplicates_keep_last(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] not in nums[i+1:]:
            result.append(nums[i])
    return result
print("26 esep: ", remove_duplicates_keep_last([1,2,3,2,4,1,5]))

#27 esep
result = lambda words: sorted(words, key = lambda x: (-len(x), x))[:5]
print("27 esep: ", result(["cat", "dog", "tiger", "lion", "bear", "elephant"]))

#28 esep
def moving_average(nums,k):
    result = []
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        negative = False
        for x in window:
            if x < 0:
                negative = True
                break
        if not negative:
            result.append(sum(window)/k)
    return result
print('28 esep: ', moving_average([1,2,3,-1,4,5,6], 3))

#29 esep
result = lambda a,b: list(filter(
    lambda x: x not in b and x > sum(a) /len(a), a
))
print("29 esep: ", result([1,5,7,2,9],[2,3,7]))

#30 esep
def analyze_strings_list(words):
    result = []
    for word in words:
        digit = False
        for i in word:
            if i.isdigit():
                digit = True
                break
        if digit:
            continue
        if len(word) % 2 == 0:
            new_w = word[::-1]
        else:
            new_w = word.upper()
        if new_w not in result:
            result.append(new_w)
    return result
print("30 esep: ", analyze_strings_list(["hello", "test1", "world", "hi", "hello", "abc"]))

#DICT AND SET
print("DICT AND SET ")
#1 esep
def invert_unique(d):
    result = {}
    for key in d:
        value = d[key]
        if value not in result:
            result[value] = []
        if key not in result[value]:
            result[value].append(key)
    return result
d = {"a": 1, "b": 2, "c": 1, "d": 2,"e": 3}
print("1 esep: ", invert_unique(d))

#2 esep
result = lambda numbers: {
    x for x in numbers
    if x > sum(numbers) / len(numbers)
    and x % 2 != 0
    and x % 5 != 0}
print("2 esep: ", result({2,3,7,9,10,15}))

#3 esep
def merge_dicts_sum(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result
print("3 esep: ", merge_dicts_sum({"a": 10, "b":20, "c":30}, {"b":5, "c":15, "d":40}))

#4 esep
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) <= 3:
            continue
        negative = False
        jup = False
        for x in s:
            if x < 0:
                negative = True
                break
            if x%2 == 0:
                jup = True
        if not negative and jup:
            result.append(s)
    return result
sets_list = [{1,2,3,4}, {1, -2,3,4},{5,7,9,11}, {2,4,6,8,10}]
print("4 esep: ", filter_sets(sets_list))

#5 esep
result = lambda d: sorted(d.keys(),
       key = lambda k: (-d[k],k))[:5]
a = {"apple":10, "banana":5, "cherry":10, "fig":5, "grape":12}
print("5 esep: ", result(a))
