def permutations(nums: list[int]) -> None:
    def backtrack(curr: list[int], choices: list[int]) -> None:
        if not choices:
            print(curr)

        for i in range(len(choices)):
            choice = choices[i]
            curr.append(choice)
    
            next_choices = choices[:i] + choices[i + 1:]

            backtrack(curr, next_choices)

            curr.pop()
    
    backtrack([], nums)


permutations([1, 2, 3])