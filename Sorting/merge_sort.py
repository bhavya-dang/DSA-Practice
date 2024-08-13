def mergeSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return merge(left_half, right_half)

def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

print(mergeSort([19, 22, 1, 8, 26, 101, 2]))