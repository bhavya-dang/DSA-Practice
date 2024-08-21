# recursive approach
def findLargestElement(arr: list[int]) -> int:
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


# sorting approach
def findLargestElement(arr: list[int]) -> int:
    # using max function
    max = max(arr)

    # sorting the array first and returning last element
    arr.sort()
    max =  arr[len(arr)-1]

    return max

print(findLargestElement([12, 11, 9, 24, 5, 120, 7, 89]))
