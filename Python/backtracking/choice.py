# Generate all the ways in which you can pick k elements from the set {1, 2, ...n}

def choice(n: int, k: int):
    total = 0
    results: list[list[int]] = []

    def bk(path: list[int], start: int):
        nonlocal total
        if len(path) == k:
            results.append(path[:])
            total += 1
            return
        
        for i in range(start, n + 1):
                    path.append(i)
                    bk(path, i + 1)
                    path.pop()

    bk([], 1)
    return (results, total)

ways, total = choice(5, 3)

print(ways, total)