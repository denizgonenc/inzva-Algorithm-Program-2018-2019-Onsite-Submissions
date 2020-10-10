n = int(input())
b = list(map(int, input().split()))

a = [b[0]]
prev = b[0]
for i in range(1, n):
    temp = b[i] * (i + 1)
    a.append(temp - prev)
    prev = temp
    
print(*a)