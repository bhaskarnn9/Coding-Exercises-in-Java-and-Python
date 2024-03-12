class QuickFind:
    def __init__(self, root):
        self.root = [i for i in range(root)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


#  Test Case
qf = QuickFind(10)
qf.union(0, 1)
qf.union(0, 2)
qf.union(0, 3)
qf.union(7, 3)
print(qf.root)

print(qf.connected(2, 7))  # True
