# pattern example:
# 1
# 1 2 
# 1 2 3

# logic: 
# in row one, 1 prints, in row 2, 1 and 2 are printed and so on
# so for each iteration, the numbers printed should match the current index of the range

def rightTriangleNumberPyramid(n:int) -> None:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

print(rightTriangleNumberPyramid(3))