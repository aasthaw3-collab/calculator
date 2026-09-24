import random
number = random.randint(1,100)
while True:
    guess=int(input("guess the number:"))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("correct")
