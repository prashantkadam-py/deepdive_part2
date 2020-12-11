import math

class Factorials(object):

    def __init__(self, length):
        self.length = length


    def __iter__(self):
        return self.FactIter(self.length)


    class FactIter(object):

        def __init__(self, length):
            self.length = length
            self.index = 0


        def __iter__(self):
            return self


        def __next__(self):
            if self.index >= self.length:
                raise StopIteration

            else:
                result = math.factorial(self.index)
                self.index += 1
                return result


if __name__ == "__main__":
    facts = Factorials(10)
    for fact in facts:
        print(fact)
