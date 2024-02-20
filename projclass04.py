import random

text_tr = None
mass_tr = [
    "Скільки у тебе друзів?"
    "Що краще не "
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
]

print("--------------------\n")
print("1. Правда")
print("2. Дія")
print("3. Вийти з гри\n")
print("--------------------\n")
ch = int(input("> "))

if ch == 1:
    print("Ви вибрали правду:")
    text_tr = mass_tr.pop(random.randint(1, 10))
    print(">",text_tr)

if ch == 2:
    print("Ви вибрали дію:")
    text_tr = mass_tr.pop(random.randint(1, 10))
    print(">",text_tr)

