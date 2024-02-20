import random

def game(randNum):
    if randNum == 0:
        print("Орел")
    elif randNum == 1:
        print("Решка")
    else:
        print("Помилка")

if __name__ == "__main__":



    while True:
        print("1. Continue\n"
              "2. Break")
        ch = int(input("> Enter your choice(Number only): "))
        if ch == 1:
            randNum = random.randint(0, 1)
            result = game(randNum)
            continue
        elif  ch == 2:
            break
        else:
            print("Enter incorrect chosen")
            continue

