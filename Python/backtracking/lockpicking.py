# Generate all permutations of numbers from 0 to 9 where two consecutive numbers are different
def solve_lock(ln: int):
    results: list[list[int]] = []

    def bk(curr_combination: list[int]):
        if len(curr_combination) == ln:
            results.append(curr_combination[:])
            return

        for i in range(ln):
            if not curr_combination or curr_combination[-1] != i:
                curr_combination.append(i)
                bk(curr_combination)
                curr_combination.pop()
    bk([])
    print(results)

solve_lock(4)