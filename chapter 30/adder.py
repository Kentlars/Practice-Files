class Adder:
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return self.data + other
    def __radd__(self, other):
        return self.__add__(other)
    __radd__ = __add__
    #def __str__(self):
    #    return 'Adder value: %s' % self.data

class Number:
    def __init__(self, value):
        self.data = value
    def __iadd__(self, other):  #__iadd__ explicit: x += y
        self.data += other      # Usually returns self
        return self

class Callee:
    def __call__(self, *pargs, **kargs): #Intercept instance calls
        print('Called:', pargs, kargs)      #Accept arbitrary arguments

class Prod:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value * other

class CallBack:
    def __init__(self, value):
        self.color = value
    def __call__(self):
        print('turn', self.color)

class Comparisons:
    data = 'Spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other         


if __name__ == '__main__':
    x = Adder(5)
    print(str(x))
    print(x + 2)
    y = Adder(5)
    print(x + y)
    print(x)

    from computers import Computer1, Computer2, Computer3

    x = Computer3(3)
    y = Computer2(4)
    print(x + y)

    for klass in (Computer1, Computer2, Computer3):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(y + 1)
        print(x + y)
