def insertionSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print(insertionSort([19, 22, 1, 8, 26, 101, 2]))