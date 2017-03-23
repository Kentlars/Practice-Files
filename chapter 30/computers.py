class Computer1:
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other
    __radd__ = __add__

class Computer2(Computer1):
    def __radd__(self, other):
        print('child class: %s' % other)
        return self.__add__(other)

class Computer3(Computer1):
    def __radd__(self, other):
        return self + other

if __name__ == '__main__':
    print('fish')
