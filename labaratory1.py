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
                    s.split()
                )
            )
        )
    )
)
text = input("4 esep: мәтін: ")
print(process(text))

#5 esep

