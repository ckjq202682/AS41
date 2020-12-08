# AS41
import random


def makequestion():
    question = ""
    for i in range(7):
        a = random.randint(0, 1)
        question = str(a) + question
    count = 0
    pa = ["Even", "Odd"]
    parity = random.choice(pa)
    for b in range(len(question)):
        if question[b] == "1":
            count = count + 1
    c = count % 2
    paritybit = 0
    if parity == "Even" and c == 1:
        paritybit = 1
    elif parity == "Odd" and c == 0:
        paritybit = 1
    print(question)
    print(parity + " parity")
    return paritybit


paritybit = makequestion()

answer = int(input("Answer:"))
if answer == paritybit:
    print("That is correct!")
else:
    print("That is not correct!")
    print("The answer is:", paritybit)
