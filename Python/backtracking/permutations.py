def permutations(nums: list[int]):

    def bk(path: list[int], available: list[int]):
        if not available:
            print(path)
        
        for i in range(len(available)):
            choice = available[i]

            path.append(choice)

            next_available = available[:i] + available[i+1:]
            bk(path, next_available)

            path.pop()

    bk([], nums)


permutations([1, 2, 3])