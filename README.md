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

## 4. Generators
- Generator functions are functions which contain atleast one yield statement.
- When Generator Function is called python returns a generator object.
- Generator implements following Protocol :
    - Generator implements Iterator protocol.
- Generators are inherently lazy iterators.
- Generators become exhausted when function returns a value.

## 5. Project3
- Process csv file efficiently. 
    - Keep memory overhead minimum.
    - Use lazy iterator and lazy evaluation
   
## 6. Project4
- Process csv files efficiently.
    - Keep memory overhead minimum.
    - Use itertools module for lazy iteration.
   
## Context Manager

- It implements following protocol : 
   - \_\_enter\_\_ :
        - This method should perform whatever setup it needs to.
        - It can optionally return an object.
   
   - \_\_exit\_\_ : 
        - Runs even if an exception occurs in with block like try-finally.
- Common Patterns :
    - open-close
    - lock-release
    - change-reset
    - start-stop
    - enter-exit

