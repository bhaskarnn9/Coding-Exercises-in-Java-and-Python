import ctypes


def make_array(new_capacity):
    return (new_capacity * ctypes.py_object)()


class DynamicArray:

    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.arr_a = make_array(self.capacity)

    def __len__(self):
        return self.length

    def _resize(self, new_capacity):
        arr_b = make_array(new_capacity)
        for i in range(self.length):
            arr_b[i] = self.arr_a[i]
        self.arr_a = arr_b
        self.capacity = new_capacity
        print('new capacity', self.capacity)

    def append(self, ele):
        print('length before appending', self.length)
        print('capacity before appending', self.capacity)
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.arr_a[self.length] = ele
        self.length += 1
        print('length after appending', self.length)


da_instance = DynamicArray()
da_instance.append(10)
da_instance.append(20)
print(da_instance.__len__())
