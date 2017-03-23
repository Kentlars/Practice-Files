#!python3
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

class SquaresYield: #__iter__ + yield generator
    def __init__(self, start, stop): #___next__ is automatic/implied
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2 #next is now automated and implied by the use of yield
            #Generator has both instance and local scope state

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2
