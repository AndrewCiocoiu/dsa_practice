def alternating_permutations(nr: int):
    def bk(path: list[int]):
        if len(path) == nr:
            print(path)
            return


        for num in range(nr):
            if num not in path:
                if not path or path[-1] % 2 != num % 2:
                    path.append(num)
                    bk(path)
                    path.pop()

    bk([])

alternating_permutations(3)