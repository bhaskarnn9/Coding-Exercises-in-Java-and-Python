"""
Creating a custom array for demonstration purpose
"""

import ctypes


def make_array(new_cap):
    return (new_cap * ctypes.py_object)()


class DynamicArray:

    def __init__(self):
        self.n = 0  # index == length
        self.capacity = 1  # no of elements
        self.A = make_array(self.capacity)  # makes an array of size equal to capacity

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!')
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if capacity isn't enough
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        b = make_array(new_cap)
        for k in range(self.n):
            b[k] = self.A[k]
        self.A = b
        self.capacity = new_cap


arr = DynamicArray()
arr.append(1)
arr.append(2)
print(len(arr))
print(arr.__getitem__(len(arr)))
