print("Hello")

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2, 2):
        if (n%i) == 0: 
            return False
    return True



