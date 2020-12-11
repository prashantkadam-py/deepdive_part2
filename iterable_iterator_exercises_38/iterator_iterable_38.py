class Cities(object):

    def __init__(self):

        self._cities = ["Mumbai", "Pune", "Bengaluru", "Hyderabad"]
    
    def __len__(self):
        return len(self._cities)


    def __iter__(self):
        print("cities __iter__ called")
        return self.CityIterator(self)

    
    def __getitem__(self, s):
        return self._cities[s]

    class CityIterator(object):

        def __init__(self, city_obj):
            print("CityIterator new object!")
            self._index = 0
            self._city_obj = city_obj

        def __iter__(self):
            print("CityIterator __iter__ called")
            return self

        def __next__(self):
            print("CityIterator __next__ called")
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item



if __name__ == "__main__":
    cities = Cities()
    for city in cities:
        print(city)
    
    city_iter_1 = cities.__iter__()
    city_iter_2 = cities.__iter__()

    print(cities[0])


