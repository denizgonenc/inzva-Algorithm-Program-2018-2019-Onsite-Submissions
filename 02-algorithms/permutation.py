n = int(input())
ar1 = list(map(int, input().split()))
ar1.sort()
ar2 = list(range(1, n+1))

operations = 0
for i in range(n):
    operations += abs(ar1[i] - ar2[i])
print(operations)