class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        path = []
        res = []
        remains = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        def back_track(remains, k, n):
            if n < 0:
                return
            if k == 0 and n == 0:
                res.append(path[::])
                return
            for num in remains:
                if path != [] and num < max(path):
                    continue
                path.append(num)
                remains.remove(num)
                back_track(remains, k-1, n-num)
                path.pop()
                remains.add(num)
        back_track(remains, k, n)

        return res
