def second_exercise_with_extras():
    num = int(input("enter a number: "))
    if num % 4 == 0:
        print("multiplication out of 4 is possible")
    elif num % 2 == 0:
        print("even")
    else:
        print("odd")

def extra2nd_part():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))

    if num1 % num2 == 2:
        print("first number divides evenly from second number")
    else:
        print("doesnt divide evenly")

extra2nd_part()