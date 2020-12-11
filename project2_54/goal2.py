from goal1 import Polygon


class PolygonIterator(object):

    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be greater than 3")
        self._m = m
        self._R = R
        self._i = 3

    def __iter__(self):
        print("PolygonIterator got called.")
        return self

    def __next__(self):
        print("PolygonIterator __next__ got called")
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i, self._R)
            self._i += 1
            return result



class Polygons(object):

    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be greater than 3")
        self._m = m
        self._R = R
        #self._polygons = [Polygon(i, R) for i in range(3, m+1)]


    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f"Polygons(m={self._m}, R={self._R})"


    #def __getitem__(self, s):
    #    return self._polygons[s]

    def __iter__(self):
        print("Polygons __iter__ got called")
        return PolygonIterator(self._m, self._R)

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(PolygonIterator(self._m, self._R),
                key = lambda p : p.area/p.perimeter,
                reverse = True
                )
        #sorted_polygons = sorted(self._polygons,
        #                        key = lambda p: p.area/p.perimeter, 
        #                        reverse = True)
        return sorted_polygons[0]

if __name__ == "__main__":

    polygons = Polygons(10, 2)
    print("Polygon Sequence : ")   
    for p in polygons:
        print(p)
    print("\n\n")
    print("Max efficiency polygon is : ")
    print(polygons.max_efficiency_polygon)
