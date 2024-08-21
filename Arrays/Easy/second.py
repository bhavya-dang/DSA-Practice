arr = [19, 1, 12, 23, 101, 6]

def secondSmallest(arr: list[int], n: int) -> int:
    if n < 2:
        return -1
    
    # # with built-in functions
    # arr.sort()

    # with one pass solution
    small = float("inf")
    second_small = float("inf")
    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    return second_small

    # return arr[1]





def secondLargest(arr: list[int], n: int) -> int:
    if n < 2:
        return -1
    
    # # with built-in functions
    # arr.sort()
    # return arr[-2]

    # with one pass solution
    large = float("-inf")
    second_large = float("-inf")
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large



print(secondSmallest(arr, len(arr)))
print(secondLargest(arr, len(arr)))