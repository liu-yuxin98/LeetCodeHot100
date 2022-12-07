

def combine(n: int, k: int) -> list[list[int]]:
    result = []
    path = []

    def backtrack(n, k, start_index):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start_index, n+1):
            path.append(i)
            backtrack(n, k, i+1)
            path.pop()
            print(i, path)
    backtrack(n, k, 1)
    return result


result = combine(4, 2)
print(result)
