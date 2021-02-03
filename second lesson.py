
def carry_solver(n1,n2):
    counter = 0
    longer_number = max(len(str(n1)), len(str(n2)))
    carry_in_mind = 0
    for i in reversed(range(longer_number)):
        carry_in_mind = n1 % 10 + n2 % 10 + carry_in_mind
        if carry_in_mind >= 10:
            carry_in_mind = 1
        else:
            carry_in_mind = 0
        counter += carry_in_mind
        n1 = n1 // 10
        n2 = n2 // 10
    if counter == 0:
        print("no carry")
    else:
        print("carry counter: " + str(counter))


carry_solver(6236667212,6736266032)


