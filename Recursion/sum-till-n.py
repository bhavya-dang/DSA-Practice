def sum_till_n(n: int) -> int:
    """Calculates the sum of all numbers from 1 to n"""
    def recursive_sum(i: int) -> int:
        if i < 1:
            return 0
        else:
            print(i, end=" + " if i > 1 else "")
            return i + recursive_sum(i-1)

    print("Numbers to add: ", end="")
    result = recursive_sum(n)
    print(" = ", result)
    return result

sum_till_n(10)