class SkipObject:
    def __init__(self, wrapped): #Save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped) # New iterator each time

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped #Iterator state information
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped): #Terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset] #else return and skip
            self.offset += 2
            return item

def gen(x): #Any function that contains a yield statement is turned into a generator function.
    for i in range(x): yield i ** 2
