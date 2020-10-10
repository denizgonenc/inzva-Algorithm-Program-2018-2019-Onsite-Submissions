def isPrime(n):
    i = 2
    while i*i < n:
        if n % i == 0:
            return "Not Prime"
        i += 1
    return "Prime"


t = int(input())
for _ in range(t):
    n = int(input())
    print(isPrime(n))