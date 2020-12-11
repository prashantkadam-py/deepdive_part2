class CyclicIterator(object):

    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self._index >= len(self._iterable):
            self._index = 0
        
        item = self._iterable[self._index]
        self._index += 1
        return item



class CyclicIterator1(object):

    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item
            

if __name__ == "__main__":
    iter_cycl = CyclicIterator1("NSWE") #CyclicIterator1("NSWE")
    for i in range(10):
        print(i, next(iter_cycl))
