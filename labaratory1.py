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

# Проверка
text = input("2 esep: мәтін: ")
print(process(text))