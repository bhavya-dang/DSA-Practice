def bubbleSort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([19, 22, 1, 8, 26, 101, 2]))