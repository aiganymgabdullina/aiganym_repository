with open("new_file","w", encoding="utf-8") as f:
    f.write("aiganym\n")
    f.write("Privet\n")

with open("numbers.txt", "w") as f1:
    for i in range(1, 11):
        f1.write(str(i) + "\n")


with open("students.txt", "w", encoding="utf-8" ) as f2:
    name = input()
    names = name.split()
    for n in names:
        f2.write(n.title() + "\n")
    print()

with open("students.txt", "r", encoding="utf-8") as f2:
    for a in f2:
        print(name.strip().title())

import csv
with open("data.csv", "w", encoding="utf-8") as f:
    f.write("aiganym")

import csv
with open("numbers.csv", "w") as f1:
    for i in range(1, 11):
        f1.write(str(i) + "\n")

import csv
with open("students.csv", "w", encoding="utf-8" ) as f2:
    name = input()
    names = name.split()
    for n in names:
        f2.write(n.title() + "\n")
    print()
with open("students.csv", "r", encoding="utf-8") as f2:
    for a in f2:
        print(name.strip().title())