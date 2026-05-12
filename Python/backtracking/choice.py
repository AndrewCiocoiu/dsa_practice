# Generate all the ways in which you can pick k elements from the set {1, 2, ...n}

def choice(n: int, k: int):
    total = 0
    results: list[list[int]] = []

    def bk(path: list[int]):
        nonlocal total
        if len(path) == k:
            results.append(path[:])
            total += 1
            return
        
        for i in range(n):
            if i not in path:
                if not path or i > path[-1]:
                    path.append(i)
                    bk(path)
                    path.pop()

    bk([])
    return (results, total)

ways, total = choice(5, 3)

print(ways, total)