# deepdive_part2

## 1. Project1
Implement Custom Sequence Type with some propertie. Use \_\_getitem\_\_ method to implement the custom sequencer. 

## 2. Iterators vs Iterables

- Iterator Implements following protocol :
    - \_\_next\_\_  : returns next item from the data collection
    - \_\_iter\_\_  : returns class instance (self)
    - Iterators exhaust.
    
- Iterable implements following protocol : 
    - \_\_iter\_\_ : returns new instance of the iterator object used to iterate over iterable.
    - Iterables are non-exhaustive.
    
- Examples : (iterable_iterator_exercises)
    - Iterator(CityIterator) - Iterable(Cities)
    - Cyclic Iterators
    - Lazy Iterables (Factorials)
    - Generic Callable Iterator
    - Delegating Iterators
    - Reversed Iteration
   
## 3. Project2
Refactor Project1 code of Polygon and Polygons. 
- Convert all the calculated Polygon properties to lazy properties.
- Convert Polygons (Sequence) type into an Iterable.

