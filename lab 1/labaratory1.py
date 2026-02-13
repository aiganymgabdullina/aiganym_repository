#1 esep
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







