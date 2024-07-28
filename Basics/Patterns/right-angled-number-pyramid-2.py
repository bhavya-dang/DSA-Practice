# pattern example:
# 1
# 2 2 
# 3 3 3

# logic: 
# in row one, 1 prints, in row 2, 2 and 2 are printed and so on
# so for each iteration, the amount of the values and the values printed should match the current index of the range

def rightTriangleNumberPyramid(n:int) -> None:
    for i in range(1, n+1):
        print(f"{i}" * i)

print(rightTriangleNumberPyramid(3))