def selectionSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1): # 0, 5
        minIndex = i # 0
        for j in range(i+1, n): # 1, 6
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp
    return arr

print(selectionSort([19, 22, 1, 8, 26, 101, 2]))