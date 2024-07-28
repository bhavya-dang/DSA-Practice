# pattern example:
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# logic: 
# in row one, 5 star prints, in row 2, 4 stars are printed and so on
# 1 -> 5, 2 -> 4, 3 -> 3, 4 -> 2, 5 -> 1

def rightTriangleReverse(n:int) -> None:
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print("*", end=" ")
        print()

print(rightTriangleReverse(5))