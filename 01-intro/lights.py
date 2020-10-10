n = int(input())
m = int(input())
k = int(input())
lights = []

if k == 0:
    print(n - m)
else:
    for _ in range(m):
        lights.append(int(input()))

    needed = 0
    for i in range(len(lights)):
        if i == 0:
            needed += (lights[0] - k - 1) // (2 * k) + 1
        if i == m-1:
            needed += (n - k - lights[m-1] - 1) //  (2 * k) + 1
        else:
            temp = lights[i]
            while lights[i+1] > (temp + 2*k + 1):
                needed += 1
                temp += 2*k + 1

    print(needed)