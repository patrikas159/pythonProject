def get_integer(text):
    return int(input(text))

def isPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    return True;


num=get_integer("nnter number: ");
if isPrime(num):
    print("number is prime")
else:
    print("number isnt prime")