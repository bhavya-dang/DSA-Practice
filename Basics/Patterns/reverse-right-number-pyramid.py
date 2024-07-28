# pattern example:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1


def rightTriangleNumberPyramidReverse(n:int) -> None:
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print(f"{j}", end=" ")
        print()

print(rightTriangleNumberPyramidReverse(6))