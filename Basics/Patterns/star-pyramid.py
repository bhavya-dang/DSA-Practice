# # pattern:
# #   *  
# #  *** 
# # ***** 

# def starPyramid(n:int) -> None:
#     for i in range(1, n+1):
#         # space
#         for j in range (1, n-i):
#             print(" ", end="")
#         print()
#         # stars
#         for j in range (1, (2*i)+1):
#             print("*", end="")
#         print()

#         #space
#         for j in range (1, n-i):
#             print(" ", end="")
#         print()

# print(starPyramid(5))

# writing to output file
def starPyramid(n: int, filename: str) -> None:
    # with open(filename, 'w') as f:
        for i in range(1, n+1):
            # space
            for j in range (1, n-i+1):
                # f.write(" ")
                print(" ", end="")
            # stars
            for j in range (1, (2*i)):
                # f.write("*")
                print("*", end="")
            print()
            # f.write("\n")

print(starPyramid(5, 'output.txt'))
