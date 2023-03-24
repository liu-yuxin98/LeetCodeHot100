class Solution:
    def Find(self, target: int, array: list[list[int]]) -> bool:
        if array == [] or len(array) == 0 or len(array[0]) == 0:
            return False
        rows = len(array)
        cols = len(array[0])
        r = 0
        c = cols-1
        while(r < rows and c > -1):
            if array[r][c] == target:
                return True
            elif array[r][c] < target:
                r += 1
            else:
                c -= 1
        return False


array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 5


sol = Solution()
res = sol.Find(target, array)
print(res)
