# Generate all the ways in which you can place n rooks on an n by n chessboard

def place_rooks(n: int):
    def bk(path: list[int]):
        if len(path) == n:
            for i in range(n):
                for j in range(n):
                    if j == path[i]:
                        print("X", end="")
                    else:
                        print("O", end="")
                print()
            print()
        
        for i in range(n):
            if not path or i not in path:
                path.append(i)
                bk(path)
                path.pop()
    bk([])

place_rooks(3)
