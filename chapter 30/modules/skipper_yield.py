class SkipObject:                #another __iter__+yield generator
    def __init__(self, wrapped): #Instance scope retained normally
        self.wrapped = wrapped   #Local scope state saved automatically
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
