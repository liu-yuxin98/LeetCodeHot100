class unionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1]*n

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]

    def find(self, x):
        # find the highest parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isConnected(self, x, y):

        return self.find(x) == self.find(y)
