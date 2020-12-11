
class SquaresIterable(object):

    def __init__(self, n):
        self._n = n


    def __iter__(self):
        return SquaresIterable.squares_gen(self._n)

    @staticmethod
    def squares_gen(n):
        for num in range(n):
            yield num ** 2



if __name__ == "__main__":

    square_iter = SquaresIterable(10)
    for i in square_iter:
        print(i)

    print(list(square_iter))
    print(list(square_iter))
    
    s_gen = SquaresIterable.squares_gen(10)
    print(list(s_gen))
    print(list(s_gen))
