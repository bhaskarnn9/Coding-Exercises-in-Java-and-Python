class UnionByPathCompression:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


#  Test Case
qf = UnionByPathCompression(10)
qf.union(0, 1)
qf.union(0, 2)
qf.union(0, 3)
qf.union(7, 3)
print(qf.root)

print(qf.connected(3, 7))  # True
