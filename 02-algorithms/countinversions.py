n = int(input())
arr = list(map(int, input().split()))
inversions = 0


def mergeSortInversion(arr):
    global inversions
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSortInversion(left)
        mergeSortInversion(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                inversions += mid - i
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


mergeSortInversion(arr)
print(inversions)