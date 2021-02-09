import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"choose number between 1 and {x}: "))
        if guess < random_number:
            print("guess too low")
        elif guess > random_number:
            print("guess too high")


    print(f"your exectly right. random number {random_number}")



guess(9)
