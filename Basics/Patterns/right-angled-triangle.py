# pattern example:
# * 
# * * 
# * * * 

# logic: 
# in row one, 1 star prints, in row 2, 2 stars are printed and so on
# so for each iteration, the value of the stars should match the current index of the range

def rightTriangle(n:int) -> None:
    for i in range(1, n+1):
        print("* " * i)

print(rightTriangle(3))