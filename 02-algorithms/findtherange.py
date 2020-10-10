nq = list(map(int, input().split()))
n, q = nq[0], nq[1]
l, r = [], []
for _ in range(n):
    temp = input().split()
    l.append(int(temp[0]))
    r.append(int(temp[1]))

while (q > 0):
    x = int(input())
    beg, end = 0, n - 1
    mid = (beg + end) // 2
    while (beg < end):
        if l[mid] > x:
            end = mid - 1
        elif r[mid] < x:
            beg = mid + 1
        else:
            break
        mid = (beg + end) // 2

    if l[mid] <= x and r[mid] >= x:
        print("Yes")
    else:
        print("No")
    q -= 1
