def counter():

    count = 0

    def inc():
        nonlocal count
        count += 1

        return count
    return inc



class CallableIterator(object):

    def __init__(self, callable_, sentinel):

        self._callable = callable_
        self._sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration

        result = self._callable()
        if result == self._sentinel:
            self.is_consumed = True
            raise StopIteration
        else:
            return result

if __name__ == "__main__":
   count = counter() 
   callable_iter = CallableIterator(count, 10)
   for count in callable_iter:
       print(count)
