import itertools

def findsubsets(ar, n):
    return list(itertools.combinations(ar, i))


n = int(input())
ar = list(map(int, input().split()))
res = abs(ar[0])
for i in range(1, n + 1):
    subsets = findsubsets(ar, i)
    for j in range(len(subsets)):
        temp = abs(sum(subsets[j]))
        if temp < res:
            res = temp

print(res)