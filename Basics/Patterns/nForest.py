# pattern of NXN matrix consisting of "*"
# example pattern:
# * * *
# * * *
# * * *

def nForest(n: int) -> None:
    for i in range(n):
        print("* " * n)

print(nForest(3))