import sys


class BFDataModel:
    def __init__(self, size=30000):
        self._data = [0 for _ in range(size)]
        self._index = 0

    @property
    def pointer(self):
        return self._index

    @pointer.setter
    def pointer(self, value):
        self._index = value % len(self._data)

    @property
    def pointee(self):
        return self._data[self._index]

    @pointee.setter
    def pointee(self, value):
        self._data[self._index] = value

    def increment_pointer(self):
        self.pointer += 1

    def decrement_pointer(self):
        self.pointer -= 1

    def increment_pointee(self):
        self.pointee += 1

    def decrement_pointee(self):
        self.pointee -= 1

    def conditional_skip(self):
        return self.pointee == 0

    def unconditional_jump(self):
        pass

    def print_pointee(self):
        print(
            chr(self.pointee), end=''
        )

    def input_to_pointee(self):
        self.pointee = ord(sys.stdin.read(1))
