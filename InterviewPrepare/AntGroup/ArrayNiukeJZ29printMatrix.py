class Solution:
    # previously I set matrix[i][j] = TRUE when reached it will cause problems since 1 == True
    def printMatrix(self, matrix: list[list[int]]) -> list[int]:
        # write code here
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directIndex = 0
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        res = []
        while True:
            if len(res) >= m*n:
                break
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == "A":
                i -= directions[directIndex % 4][0]
                j -= directions[directIndex % 4][1]
                # change direction
                directIndex += 1
                # one step forward
                i += directions[directIndex % 4][0]
                j += directions[directIndex % 4][1]
            else:
                res.append(matrix[i][j])
                matrix[i][j] = "A"
                i += directions[directIndex % 4][0]
                j += directions[directIndex % 4][1]

        return res


matrix = [[1, 2], [4, 3]]

sol = Solution()
res = sol.printMatrix(matrix)
print(res)
